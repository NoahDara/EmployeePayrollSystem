from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from notification.views import (
    MarkAllAsReadView,
    NotificationsListView, GenericCommentCreateView, CommentUpdateView, CommentDeleteView
    )

urlpatterns = [
    path('mark-all-as-read/', MarkAllAsReadView.as_view(), name='mark_all_as_read'),
    path('all-notifications/', NotificationsListView.as_view(), name='all_notifications'),
    
    path("comment/<int:content_type_id>/<int:object_id>/<str:comment_type>/add/", 
         GenericCommentCreateView.as_view(), name="add_generic_comment"),
    
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/delete/", CommentDeleteView.as_view(), name="comment-delete")
] 
