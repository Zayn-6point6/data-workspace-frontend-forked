from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView

from dataworkspace.apps.applications.models import ApplicationInstance
from dataworkspace.apps.datasets.models import VisualisationCatalogueItem
from dataworkspace.apps.datasets.utils import find_dataset_or_visualisation
from dataworkspace.apps.eventlog.models import EventLog
from dataworkspace.apps.eventlog.utils import log_event
from dataworkspace.apps.request_access.forms import (  # pylint: disable=import-error
    DatasetAccessRequestForm,
    ToolsAccessRequestFormPart1,
    ToolsAccessRequestFormPart2,
    ToolsAccessRequestFormPart3,
)

from dataworkspace.apps.request_access import models
from dataworkspace import zendesk


class DatasetAccessRequest(CreateView):
    model = models.AccessRequest
    template_name = 'request_access/dataset.html'
    form_class = DatasetAccessRequestForm

    def get_initial(self):
        return {'contact_email': self.request.user.email}

    def get_context_data(self, **kwargs):
        user_has_tools_access = self.request.user.user_permissions.filter(
            codename='start_all_applications',
            content_type=ContentType.objects.get_for_model(ApplicationInstance),
        ).exists()
        catalogue_item = find_dataset_or_visualisation(
            self.kwargs['dataset_uuid'], self.request.user
        )
        context = super().get_context_data(**kwargs)
        context['catalogue_item'] = catalogue_item
        context['is_visualisation'] = isinstance(
            catalogue_item, VisualisationCatalogueItem
        )
        context['user_has_tools_access'] = user_has_tools_access
        return context

    def dispatch(self, request, *args, **kwargs):
        user_has_tools_access = request.user.user_permissions.filter(
            codename='start_all_applications',
            content_type=ContentType.objects.get_for_model(ApplicationInstance),
        ).exists()

        if 'dataset_uuid' in self.kwargs:
            catalogue_item = find_dataset_or_visualisation(
                self.kwargs['dataset_uuid'], request.user
            )
            user_has_dataset_access = catalogue_item.user_has_access(self.request.user)
        else:
            catalogue_item = None
            user_has_dataset_access = True

        if user_has_dataset_access and not user_has_tools_access:
            access_request = models.AccessRequest.objects.create(
                requester=self.request.user,
                catalogue_item_id=catalogue_item.id if catalogue_item else None,
            )
            return HttpResponseRedirect(
                reverse('request-access:tools-1', kwargs={"pk": access_request.pk})
            )
        elif user_has_dataset_access and user_has_tools_access:
            return render(request, 'request_access/you_have_access.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user_has_tools_access = self.request.user.user_permissions.filter(
            codename='start_all_applications',
            content_type=ContentType.objects.get_for_model(ApplicationInstance),
        ).exists()
        catalogue_item = find_dataset_or_visualisation(
            self.kwargs['dataset_uuid'], self.request.user
        )

        access_request = models.AccessRequest.objects.create(
            requester=self.request.user,
            catalogue_item_id=catalogue_item.id,
            contact_email=form.cleaned_data['contact_email'],
            reason_for_access=form.cleaned_data['reason_for_access'],
        )

        if user_has_tools_access or isinstance(
            catalogue_item, VisualisationCatalogueItem
        ):
            return HttpResponseRedirect(
                reverse('request-access:summary-page', kwargs={"pk": access_request.pk})
            )
        return HttpResponseRedirect(
            reverse('request-access:tools-1', kwargs={"pk": access_request.pk})
        )


class DatasetAccessRequestUpdate(UpdateView):
    model = models.AccessRequest
    template_name = 'request_access/dataset.html'
    form_class = DatasetAccessRequestForm

    def get_success_url(self):
        if self.object.journey == self.object.JOURNEY_DATASET_ACCESS:
            return reverse('request-access:summary-page', kwargs={"pk": self.object.pk})
        return reverse('request-access:tools-1', kwargs={"pk": self.object.pk})


class ToolsAccessRequestPart1(UpdateView):
    model = models.AccessRequest
    template_name = 'request_access/tools_1.html'
    form_class = ToolsAccessRequestFormPart1

    def get_success_url(self):
        return reverse('request-access:tools-2', kwargs={"pk": self.object.pk})


class ToolsAccessRequestPart2(UpdateView):
    model = models.AccessRequest
    template_name = 'request_access/tools_2.html'
    form_class = ToolsAccessRequestFormPart2

    def get_success_url(self):
        if self.object.spss_and_stata:
            return reverse('request-access:tools-3', kwargs={"pk": self.object.pk})
        return reverse('request-access:summary-page', kwargs={"pk": self.object.pk})


class ToolsAccessRequestPart3(UpdateView):
    model = models.AccessRequest
    template_name = 'request_access/tools_3.html'
    form_class = ToolsAccessRequestFormPart3

    def get_success_url(self):
        return reverse('request-access:summary-page', kwargs={"pk": self.object.pk})


class AccessRequestSummaryPage(DetailView):
    model = models.AccessRequest
    template_name = 'request_access/summary.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['catalogue_item'] = (
            find_dataset_or_visualisation(
                ctx['object'].catalogue_item_id, self.request.user
            )
            if ctx['object'].catalogue_item_id
            else None
        )
        return ctx

    def post(self, request, pk):
        return HttpResponseRedirect(
            reverse('request-access:confirmation-page', kwargs={"pk": pk})
        )


class AccessRequestConfirmationPage(DetailView):
    model = models.AccessRequest
    template_name = 'request_access/confirmation-page.html'

    def get(self, request, *args, **kwargs):
        access_request = self.get_object()
        if not access_request.zendesk_reference_number:
            catalogue_item = (
                find_dataset_or_visualisation(
                    access_request.catalogue_item_id, self.request.user
                )
                if access_request.catalogue_item_id
                else None
            )

            if (
                isinstance(catalogue_item, VisualisationCatalogueItem)
                and catalogue_item.visualisation_template is not None
            ):
                access_request.zendesk_reference_number = zendesk.notify_visualisation_access_request(
                    request, access_request, catalogue_item,
                )
            else:
                access_request.zendesk_reference_number = zendesk.create_zendesk_ticket(
                    request, access_request, catalogue_item,
                )
            access_request.save()

            if catalogue_item:
                log_event(
                    request,
                    EventLog.TYPE_DATASET_ACCESS_REQUEST,
                    catalogue_item,
                    extra={
                        'ticket_reference': access_request.zendesk_reference_number,
                    },
                )
            else:
                log_event(
                    request,
                    EventLog.TYPE_TOOLS_ACCESS_REQUEST,
                    extra={
                        'ticket_reference': access_request.zendesk_reference_number,
                    },
                )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogue_item'] = (
            find_dataset_or_visualisation(
                self.object.catalogue_item_id, self.request.user
            )
            if self.object.catalogue_item_id
            else None
        )
        return context
