from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 10
    list_per_page = 20
