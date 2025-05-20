from django.contrib import admin
from .models import Employment , Exit
# Register your models here.
@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'job_title', 'job_grade', 'company', 'branch', 'engagement_date', 'supervisor', 'status' )
    list_filter = ('job_title', 'status', 'company', 'branch' )
    search_fields = ('employee__fist_name', 'employee__last_name', 'job_title', 'job_grade', 'company__name', 'branch__name', 'supervisor__fist_name', 'supervisor__last_name')
    date_hierarchy = 'updated'
    
@admin.register(Exit)
class ExitAdmin(admin.ModelAdmin):
    list_display = ('employment', 'exit_type', 'exit_date', 'is_finalized',  )
    list_filter = ('exit_type', )
    search_fields = ('employment__employee__fist_name',)
    date_hierarchy = 'updated'