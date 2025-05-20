from django.contrib import admin
from .models import Language, MaritalStatus, DisabilityStatus, Race
# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'created',  )
    list_filter = ('is_active', )
    search_fields = ('name', 'code',)
    date_hierarchy = 'updated'
    
@admin.register(MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'code', 'is_active', 'created',  )
    list_filter = ('is_active', )
    search_fields = ('status', 'code',)
    date_hierarchy = 'updated'
    
@admin.register(DisabilityStatus)
class DisabilityStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'code', 'is_active', 'created',  )
    list_filter = ('is_active', )
    search_fields = ('status', 'code',)
    date_hierarchy = 'updated'
    
@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'created',  )
    list_filter = ('is_active', )
    search_fields = ('name', 'code',)
    date_hierarchy = 'updated'