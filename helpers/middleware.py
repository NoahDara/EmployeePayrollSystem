import logging
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
import threading

from notification.helpers import send_email_from_global_config
_user = threading.local()
logger = logging.getLogger(__name__)
from django.views import debug  

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Still keep this for early-stage issues
        logger.info("⚠️ Entered ErrorHandlingMiddleware")
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.exception("✅ process_exception caught an error")

        User = get_user_model()
        try:
            superuser = User.objects.filter(is_superuser=True).first()
        except Exception:
            superuser = None

        if superuser and superuser.email:
            email_subject = "🚨 Unhandled Exception in Application"
            email_content = f"""
                A critical error occurred in the application.

                Path: {request.path}
                Error: {str(exception)}

                Please investigate.
            """
            send_email_from_global_config(email_subject, superuser, email_content)

        context = {
            "message": "An unexpected error occurred. Our team has been notified.",
            "request_path": request.path,
            "error": str(exception)
        }

        return render(request, "errors/500.html", context=context, status=500)
        
    


class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _user.value = request.user
        response = self.get_response(request)
        return response

def get_current_user():
    return getattr(_user, 'value', None)