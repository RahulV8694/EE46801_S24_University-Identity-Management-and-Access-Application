from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('professor/', views.professor, name='professor'),
    path('professor_valid/<str:professor_id>/', views.professor_valid, name='professor_valid'),
    path('student/', views.student, name='student'),
    path('department_semester_form/',views.department_semester_form,name='department_semester_form')
]

