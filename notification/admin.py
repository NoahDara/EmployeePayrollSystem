from django.contrib import admin
from notification.models import Notification, Comment

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'user', 'status', 'created', 'updated')
    list_filter = ('status', 'created',)
    search_fields = ('model',)
    date_hierarchy = 'created'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_by',  'comment_type',  'content_type', 'object_id',  'is_viewed',  'created')
    search_fields = ('comment_type',)
    list_filter = ('comment_type', 'content_type',)
    date_hierarchy = 'created'