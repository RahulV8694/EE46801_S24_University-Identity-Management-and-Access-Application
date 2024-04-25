from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "dept_name", "salary")
    list_filter = ("dept_name",)
    search_fields = ("name", "dept_name", "salary")
    ordering = ("name",)

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class DepartmentDropdownFilter(admin.SimpleListFilter):
    title = _("department")
    parameter_name = "dept_name"

    def lookups(self, request, model_admin):
        department_names = set([c.dept_name for c in Salary.objects.all()])
        return [(dept_name, dept_name) for dept_name in department_names]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(dept_name=self.value())
        return queryset


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ("dept_name", "min_salary", "max_salary", "avg_salary")
    list_filter = (DepartmentDropdownFilter,)
    search_fields = ("dept_name",)

    def get_ordering(self, request):
        return ["dept_name"]


@admin.register(InstructorProxy)
class InstructorReportAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "dept_name",
        "sections_taught",
        "students_taught",
        "total_funding",
        "papers_published",
    )

    def get_queryset(self, request):
        # Use the correct related_name 'teachings' in prefetch_related
        qs = super().get_queryset(request)
        qs = qs.prefetch_related(
            "teachings", "professorfunding_set", "professorpublications_set"
        )
        return qs

    def sections_taught(self, obj):
        return obj.teachings.count()

    sections_taught.admin_order_field = "teaches__count"
    sections_taught.short_description = "Sections Taught"

    def students_taught(self, obj):
        teaches = obj.teachings.all()
        count = 0
        for teach in teaches:
            count += teach.studentcourse_set.count()
        return count

    students_taught.short_description = "Students Taught"

    def total_funding(self, obj):
        # Aggregate the total funding for the professor
        return obj.professorfunding_set.aggregate(total=Sum("amount"))["total"] or 0

    total_funding.short_description = "Total Funding"

    def papers_published(self, obj):
        # Count the papers published by the professor
        return obj.professorpublications_set.count()

    papers_published.short_description = "Papers Published"
