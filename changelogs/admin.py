from django.contrib import admin
from .models import (
    ChangeLog,
)
# Register your models here.

@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ( 'field_name', 'old_value', 'new_value', 'content_type', 'object_id', 'content_object', 'changed_by')
    search_fields = ('field_name',)
    list_filter = ('content_type', 'changed_by')
    readonly_fields = ('timestamp',)
