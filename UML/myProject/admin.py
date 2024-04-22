from django.contrib import admin
from .models import Instructor, Teaches, Student, Takes

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'dept_name', 'salary')

@admin.register(Teaches)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'sec_id', 'semester', 'year', 'teacher_id')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'dept_name', 'total_credits')

@admin.register(Takes)
class TakesAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id', 'sec_id', 'semester', 'year', 'grade')
