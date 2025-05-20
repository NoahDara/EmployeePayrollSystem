from notification.helpers.comment import create_generic_comment
from notification.models import Comment, Notification
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from employees.models import Employee
from django.shortcuts import get_object_or_404, redirect

class MarkAllAsReadView(TemplateView):
    template_name = 'layouts/header.html'

    def get(self, request, *args, **kwargs):
        employee = Employee.objects.filter(user=request.user).first()
        if employee:
            notifications = Notification.objects.filter(employee=employee, status='pending')
            if notifications:
                for notification in notifications:
                    notification.status = 'Viewed'
                    notification.save()
                    messages.info(request, f'All notifications have been marked as read.')
            else:
                messages.info(request, 'No unread notifications.')

        return redirect(reverse('dashboard'))
    

class NotificationsListView(ListView):
    model = Notification
    template_name = 'notifications/system/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.request.user.employee.first() if hasattr(self.request.user, 'employee') else None
        context['notifications'] = Notification.objects.filter(employee=employee).order_by('-created')
        return context
    



class GenericCommentCreateView(LoginRequiredMixin, TemplateView):
    def post(self, request, content_type_id, object_id, comment_type="GENERAL", *args, **kwargs):
        comment_text = request.POST.get("comment")

        if not comment_text:
            messages.error(request, "Comment cannot be empty.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        content_type = get_object_or_404(ContentType, pk=content_type_id)
        target_model = content_type.model_class()
        target_object = get_object_or_404(target_model, pk=object_id)

        create_generic_comment(
            user=request.user, 
            comment_text=comment_text,
            comment_type=comment_type,
            target_object=target_object,
        )

        messages.success(request, "Comment added successfully.")
        return redirect(request.META.get("HTTP_REFERER", "/"))
    
class CommentUpdateView(LoginRequiredMixin, TemplateView):
    def post(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        comment_text = request.POST.get('comment')
        comment.comment = comment_text
        comment.save()
        return redirect(request.META.get("HTTP_REFERER", "/"))
    
class CommentDeleteView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        comment = Comment.objects.get(pk=self.request.GET.get('pk'))
        comment.is_deleted = True
        comment.save()
        messages.warning(self.request, 'Comment Deleted successfully')
        return redirect(request.META.get("HTTP_REFERER", "/"))