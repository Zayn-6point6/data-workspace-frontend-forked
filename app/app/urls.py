import logging

from django.contrib import (
    admin,
)
from django.contrib.auth import (
    SESSION_KEY,
    BACKEND_SESSION_KEY,
    HASH_SESSION_KEY,
    authenticate,
)
from django.http import (
    HttpResponseForbidden,
)
from django.contrib.sessions.backends.base import (
    CreateError,
)
from django.urls import (
    path,
)
from django.views.decorators.csrf import (
    csrf_exempt,
)

from app.views import (
    root_view,
    table_data_view,
    appstream_view,
    public_error_403_html_view,
    public_error_404_html_view,
    public_error_500_html_view,
    application_spawning_html_view,
    application_api_view,
)
from app.views_healthcheck import (
    healthcheck_view,
)

logger = logging.getLogger('app')


def login_required(func):
    def _login_required(request, *args, **kwargs):
        user = authenticate(request)
        if user is None:
            logger.error('Unauthenticated %s', request)
            return HttpResponseForbidden()

        request.user = user
        session = request.session

        # The session cookie is created by the proxy, but the Django session
        # implementation does not support the case where the session has not
        # been created in the cache (just as an empty dict), but the session
        # cookie already exists
        if session.cache_key not in session._cache:
            try:
                session.save(must_create=True)
            except CreateError:
                # Between checking if the key exists and creating the session
                # there could have been a parallel request
                pass

        # We perform a manual "login" for the admin application, since we
        # only decorate the admin login view, and the other admin views
        # require keys set on the session. We don't use Django's default
        # "login" function since it creates a new session cookie to avoid a
        # session fixation attack. Since we're using the same cookie as the
        # proxy, which performs its own session fixation mitigation, this is
        # acceptable
        #
        # Note that for _all_ requests the proxy confirms the session cookie
        # corresponds to an active token with SSO, so it is acceptable
        # to assume that once a request reaches the Django application,
        # the request has been authenticated
        if BACKEND_SESSION_KEY not in session:
            session[BACKEND_SESSION_KEY] = user.backend

        if SESSION_KEY not in session:
            session[SESSION_KEY] = user.id

        if HASH_SESSION_KEY not in session:
            session[HASH_SESSION_KEY] = user.get_session_auth_hash()

        return func(request, *args, **kwargs)
    return _login_required


admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('', login_required(root_view), name='root'),
    path('error_403', public_error_403_html_view),
    path('error_404', public_error_404_html_view),
    path('error_500', public_error_500_html_view),
    path('admin/', admin.site.urls),
    path('table_data/<str:database>/<str:schema>/<str:table>',
         login_required(table_data_view), name='table_data'),
    path('appstream/', login_required(appstream_view)),
    path('application/<str:public_host>/spawning', login_required(application_spawning_html_view)),
    path('api/v1/application/<str:public_host>', csrf_exempt(login_required(application_api_view))),
    path('healthcheck', healthcheck_view),  # No authentication
]

handler403 = public_error_403_html_view
handler404 = public_error_404_html_view
handler500 = public_error_500_html_view
