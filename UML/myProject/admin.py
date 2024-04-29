from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, Sum
from .models import *
from django.db.models import Sum  # Import Sum for aggregation


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
        department_names = (
            Salary.objects.order_by("dept_name")
            .values_list("dept_name", flat=True)
            .distinct()
        )
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
