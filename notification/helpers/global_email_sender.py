
from django.core.mail import EmailMultiAlternatives
# from core.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string
from django.conf import settings


def send_email_from_global_config(email_subject, user, email_content):
    email_html_content = render_to_string(
        "notifications/global_email.html",
        {"username": user.username, "your_email_content": email_content}
    )

    email_message = EmailMultiAlternatives(
        email_subject,
        email_html_content,
        settings.DEFAULT_FROM_EMAIL,
        [user.email]
    )
    email_message.content_subtype = "html"  # Set content type to HTML

    try:
        email_message.send()
        print(f"Email sent to {user.email}")
        return True
    except Exception as e:
        error_message = f"Failed to send email to {user.email}: {str(e)}"
        print(error_message)
        return False