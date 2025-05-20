from django.contrib.contenttypes.models import ContentType
from ..models import Comment

def create_generic_comment(user, comment_text, comment_type, target_object):
    """
    Create a generic comment linked to any model instance via generic foreign key.

    Args:
        user (User): The user creating the comment.
        comment_text (str): The comment body text.
        comment_type (str): The type of comment (must match COMMENT_TYPE_CHOICES).
        target_object (models.Model): The instance to which the comment is attached.

    Returns:
        Comment: The created comment instance.
    """
    content_type = ContentType.objects.get_for_model(target_object.__class__)
    comment = Comment.objects.create(
        created_by=user,
        comment=comment_text,
        comment_type=comment_type,
        content_type=content_type,
        object_id=target_object.pk,
    )
    return comment