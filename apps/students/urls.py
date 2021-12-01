from django.urls import path

from .views import (
    DownloadCSVViewdownloadcsv,
    StudentBulkUploadView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    AdmissionListView,
    AdmissionDeleteView,
    AdmissionDetailView,
)

urlpatterns = [
    path("ad_list/", AdmissionListView.as_view(), name="admission-list"),
    path("list/", StudentListView.as_view(), name="student-list"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("admission_pk/<int:pk>/", AdmissionDetailView.as_view(), name="admission-detail"),
    path("create/", StudentCreateView.as_view(), name="student-create"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),
    path("admission_pk/delete/<int:pk>/",AdmissionDeleteView.as_view(), name="admission-delete"),
    path("upload/", StudentBulkUploadView.as_view(), name="student-upload"),
    path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
]
