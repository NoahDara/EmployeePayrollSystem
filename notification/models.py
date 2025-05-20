from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
User = get_user_model()

class Notification(models.Model):
    NOTIFICATION_CHOICES = (("viewed", "Viewed"), ("pending", "Pending"))

    object_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=NOTIFICATION_CHOICES, default="pending")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False) 

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.description
    


class Comment(models.Model):
    COMMENT_TYPE_CHOICES = [
        ('APPROVAL', 'Approval Comment'),
        ('DENIAL', 'Denial Comment'),
        ('SUBMISSION', 'Submission Comment'),
        ('PROGRESS_TRACKING', 'Progress Tracking'),
        ('GENERAL', 'General Comment'),
    ]    
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='comments')
    comment_type = models.CharField(max_length=100, choices=COMMENT_TYPE_CHOICES, default="GENERAL")
    comment = models.TextField()
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')    
    
    is_viewed = models.BooleanField(default=False)  
    is_deleted = models.BooleanField(default=False) 
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment_type} by {self.created_by}"    