from django.contrib import messages
from django.http import Http404
from django.views.generic import DetailView
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.shortcuts import redirect
from dataworkspace.apps.eventlog.models import EventLog
from dataworkspace.apps.eventlog.utils import log_event
from dataworkspace.apps.data_collections.models import (
    Collection,
    CollectionDatasetMembership,
    CollectionVisualisationCatalogueItemMembership,
)
from dataworkspace.apps.datasets.models import DataSet


def get_authorised_collection(request, collection_id):
    collection_object = Collection.objects.live().get(id=collection_id)
    if request.user.is_superuser or (
        collection_object.published and request.user == collection_object.owner
    ):
        return collection_object
    else:
        raise Http404


class CollectionsDetailView(DetailView):
    template_name = "data_collections/collection_detail.html"

    def get_object(self, queryset=None):
        return get_authorised_collection(self.request, self.kwargs["collections_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        source_object = self.get_object()
        context["source_object"] = source_object
        context["dataset_collections"] = source_object.dataset_collections.filter(deleted=False)
        context["visualisation_collections"] = source_object.visualisation_collections.filter(
            deleted=False
        )

        return context


@require_http_methods(["POST"])
def delete_datasets_membership(request, collections_id, data_membership_id):
    collection = get_authorised_collection(request, collections_id)
    membership = CollectionDatasetMembership.objects.get(id=data_membership_id)

    # The membership ID doesn't match the collection ID in the URL
    if membership.collection.id != collection.id:
        raise Http404

    membership.delete(request.user)
    messages.success(request, f"{membership.dataset.name} has been removed from this collection.")

    return redirect("data_collections:collections_view", collections_id=collections_id)


@require_http_methods(["POST"])
def delete_visualisation_membership(request, collections_id, visualisation_membership_id):
    collection = get_authorised_collection(request, collections_id)
    membership = CollectionVisualisationCatalogueItemMembership.objects.get(
        id=visualisation_membership_id
    )

    # The membership ID doesn't match the collection ID in the URL
    if membership.collection.id != collection.id:
        raise Http404

    membership.delete(request.user)
    messages.success(
        request, f"{membership.visualisation.name} has been removed from this collection."
    )

    return redirect("data_collections:collections_view", collections_id=collections_id)


@require_http_methods(["POST"])
def add_dataset_to_collection(request, collections_id, dataset_id):
    collection = get_authorised_collection(request, collections_id)
    dataset_object = DataSet.objects.get(id=dataset_id)

    try:
        CollectionDatasetMembership.objects.get(
            collection=collection, dataset=dataset_object
        )

    except CollectionDatasetMembership.DoesNotExist:
        with transaction.atomic():
            CollectionDatasetMembership.objects.create(
                collection=collection, dataset=dataset_object
            )
            log_event(
                request.user,
                EventLog.TYPE_ADD_DATASET_TO_COLLECTION,
                related_object=dataset_object,
            )
    messages.success(request, f"{dataset_object.name} has been added to this collection.")

    return redirect("data_collections:collections_view", collections_id=collections_id)
