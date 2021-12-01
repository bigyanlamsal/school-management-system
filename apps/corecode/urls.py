from django.urls import path

from .views import (
    ClassCreateView,
    ClassDeleteView,
    ClassListView,
    ClassUpdateView,
    CurrentSessionAndTermView,
    IndexView,
    SessionCreateView,
    SessionDeleteView,
    SessionListView,
    SessionUpdateView,
    SiteConfigView,
    SubjectCreateView,
    SubjectDeleteView,
    SubjectListView,
    SubjectUpdateView,
    TermCreateView,
    TermDeleteView,
    TermListView,
    TermUpdateView,
)

urlpatterns = [
    path("login_admin/", IndexView.as_view(), name="home"),
    
    path("login_admin/site-config", SiteConfigView.as_view(), name="configs"),


    path(
        "current-session/", CurrentSessionAndTermView.as_view(), name="current-session"
    ),
    path("login_admin/session/list/", SessionListView.as_view(), name="sessions"),
    path("login_admin/session/create/", SessionCreateView.as_view(), name="session-create"),
    path(
        "session/<int:pk>/update/",
        SessionUpdateView.as_view(),
        name="session-update",
    ),
    path(
        "session/<int:pk>/delete/",
        SessionDeleteView.as_view(),
        name="session-delete",
    ),
    path("login_admin/term/list/", TermListView.as_view(), name="terms"),
    path("login_admin/term/create/", TermCreateView.as_view(), name="term-create"),
    path("login_admin/term/<int:pk>/update/", TermUpdateView.as_view(), name="term-update"),
    path("login_admin/term/<int:pk>/delete/", TermDeleteView.as_view(), name="term-delete"),
    path("login_admin/class/list/", ClassListView.as_view(), name="classes"),
    path("login_admin/class/create/", ClassCreateView.as_view(), name="class-create"),
    path("login_admin/class/<int:pk>/update/", ClassUpdateView.as_view(), name="class-update"),
    path("login_admin/class/<int:pk>/delete/", ClassDeleteView.as_view(), name="class-delete"),
    path("login_admin/subject/list/", SubjectListView.as_view(), name="subjects"),
    path("login_admin/subject/create/", SubjectCreateView.as_view(), name="subject-create"),
    path(
        "subject/<int:pk>/update/",
        SubjectUpdateView.as_view(),
        name="subject-update",
    ),
    path(
        "subject/<int:pk>/delete/",
        SubjectDeleteView.as_view(),
        name="subject-delete",
    ),
    
]
