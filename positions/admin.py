from django.contrib import admin
from .models import JobGrade, JobTitle
# Register your models here.
@admin.register(JobGrade)
class JobGradeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'minimum_salary', 'maximum_salary', 'is_active', )
    list_filter = ('created', 'is_active',)
    search_fields = ('name', 'code',)
    date_hierarchy = 'updated'

@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('job_grade',  'section',  'title', 'code',  'is_active',  'updated')
    search_fields = ('title', 'code')
    list_filter = ('is_active', 'updated', 'job_grade')
    date_hierarchy = 'updated'