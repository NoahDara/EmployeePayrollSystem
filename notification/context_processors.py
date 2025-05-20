from django.core.exceptions import ObjectDoesNotExist
from notification.models import Notification
from django.conf import settings
from django.contrib.auth.decorators import login_required 
from employees.models import Employee

def notification(request):
    try:
        if not request.user.is_authenticated:
            return {}  
        
        employee = Employee.objects.get(user=request.user)
        notifications = Notification.objects.filter(user=request.user, status='pending').order_by('-created')[:5]
    except ObjectDoesNotExist:
        notifications = Notification.objects.none()

    return {'notifications': notifications, 'notification_count': notifications.count()}