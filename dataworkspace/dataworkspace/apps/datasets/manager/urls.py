from django.urls import path

from dataworkspace.apps.accounts.utils import login_required
from dataworkspace.apps.datasets.manager.views import (
    DatasetManageSourceTableColumnConfigView,
    DatasetManageSourceTableView,
    SourceTableRestoreFailedView,
    SourceTableRestoreSuccessView,
    SourceTableRestoreView,
    SourceTableRestoringView,
    SourceTableUploadCreatingTableView,
    SourceTableUploadFailedView,
    SourceTableUploadIngestingView,
    SourceTableUploadRenamingTableView,
    SourceTableUploadSuccessView,
    SourceTableUploadValidatingView,
)


urlpatterns = [
    path(
        "/<uuid:source_uuid>",
        login_required(DatasetManageSourceTableView.as_view()),
        name="manage-source-table",
    ),
    path(
        "/<uuid:source_uuid>/columns",
        login_required(DatasetManageSourceTableColumnConfigView.as_view()),
        name="manage-source-table-column-config",
    ),
    path(
        "/<uuid:source_uuid>/upload/validating",
        login_required(SourceTableUploadValidatingView.as_view()),
        name="upload-validating",
    ),
    path(
        "/<uuid:source_uuid>/upload/creating-table",
        login_required(SourceTableUploadCreatingTableView.as_view()),
        name="upload-creating-table",
    ),
    path(
        "/<uuid:source_uuid>/upload/ingesting",
        login_required(SourceTableUploadIngestingView.as_view()),
        name="upload-ingesting",
    ),
    path(
        "/<uuid:source_uuid>/upload/renaming-table",
        login_required(SourceTableUploadRenamingTableView.as_view()),
        name="upload-renaming-table",
    ),
    path(
        "/<uuid:source_uuid>/upload/success",
        login_required(SourceTableUploadSuccessView.as_view()),
        name="upload-success",
    ),
    path(
        "/<uuid:source_uuid>/upload/failed",
        login_required(SourceTableUploadFailedView.as_view()),
        name="upload-failed",
    ),
    path(
        "/<uuid:source_uuid>/restore/<int:version_id>",
        login_required(SourceTableRestoreView.as_view()),
        name="restore-table",
    ),
    path(
        "/<uuid:source_uuid>/restore-table/<int:version_id>/restoring",
        login_required(SourceTableRestoringView.as_view()),
        name="restoring-table",
    ),
    path(
        "/<uuid:source_uuid>/restore-table/<int:version_id>/failed",
        login_required(SourceTableRestoreFailedView.as_view()),
        name="restore-failed",
    ),
    path(
        "/<uuid:source_uuid>/restore-table/<int:version_id>/success",
        login_required(SourceTableRestoreSuccessView.as_view()),
        name="restore-success",
    ),
]