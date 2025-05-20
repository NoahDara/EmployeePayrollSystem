from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_number', 'national_id', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'is_active' )
    list_filter = ('is_active', 'gender', 'date_of_birth')
    search_fields = ('employee_number', 'national_id', 'middle_name', 'last_name', )
    date_hierarchy = 'updated'