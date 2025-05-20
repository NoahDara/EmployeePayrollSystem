from django.core.mail import send_mail
from django.conf import settings

# Function to notify user of changes
def notify_users_on_changes(user_to_notify, change, model_name):
    """
    Notify users about changes in a particular model. ie: submissions etc
    """
    send_mail(
        f"Update to {model_name}",
        f"A {model_name} has been updated to {change} and is awaiting your action",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_to_notify.email],
    )
    