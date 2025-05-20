import logging
from django.conf import settings
from notification.models import Notification

logger = logging.getLogger(__name__)

def create_notification(object, employee, content):
    notification = Notification.objects.create(
        object_id=object.pk,
        content_type=object._meta.model_name,
        employee=employee,
        description=content,
        status='pending'
    )

    logger.info(f"Notification created for: {employee}")
