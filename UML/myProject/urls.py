from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", views.home, name="home"),
    path("university", views.uni_home, name="home"),
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
]
