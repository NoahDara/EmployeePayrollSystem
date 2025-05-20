from django.contrib import admin
from .models import Department, Section
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'created',  )
    list_filter = ('is_active', )
    search_fields = ('name', 'code',)
    date_hierarchy = 'updated'
    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('department', 'name', 'code', 'is_active', 'created',  )
    list_filter = ('is_active', 'department' )
    search_fields = ('name', 'code',)
    date_hierarchy = 'updated'