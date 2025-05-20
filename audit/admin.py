from django.contrib import admin

from audit.models import LoginHistory, NavigationEvent

# Register your models here.
@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'channel', 'login_time')
    list_filter = ('user', 'channel')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    date_hierarchy = 'login_time'
    
@admin.register(NavigationEvent)
class NavigationEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'method', 'url', 'timestamp')
    list_filter = ('method', 'timestamp')
    search_fields = ('user__username', 'user__first_name', 'url')
    date_hierarchy = 'timestamp'
