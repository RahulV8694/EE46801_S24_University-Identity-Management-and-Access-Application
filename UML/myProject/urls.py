from . import views
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("professor/", views.professor, name="professor"),
    path(
        "professor_valid/<str:professor_id>/",
        views.professor_valid,
        name="professor_valid",
    ),
    path("student/", views.student, name="student"),
    path(
        "department_semester_form/",
        views.department_semester_form,
        name="department_semester_form",
    ),
    path("professor/logout/", views.professor_logout, name="prof_logout"),
    path("student/logout/", views.student_logout, name="stu_logout"),
    path("admin-page/", RedirectView.as_view(url="/admin/"), name="admin"),
    path("performance/", views.instructor_performance, name="instructor_performance"),
]
