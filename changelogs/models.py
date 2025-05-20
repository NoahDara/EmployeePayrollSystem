from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from helpers.middleware import get_current_user
User = get_user_model()


class ChangeLog(models.Model):
    field_name = models.CharField(max_length=255)
    old_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')    
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="changelogs")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        if self.old_value == self.new_value:
            if self.pk:
                super().delete()
            return  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.content_type} #{self.object_id} {self.field_name} changed from {self.old_value} to {self.new_value}"


class TrackChangesModel(models.Model):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.pk:
            self._initial_state = self._dict

    @property
    def _dict(self):
        try:
            return {
                f.name: getattr(self, f.name)
                for f in self._meta.fields
                if f.name != 'id'
            }
        except RecursionError:
            return {}

    def save(self, *args, **kwargs):
        if self.pk:
            old = self.__class__.objects.get(pk=self.pk)
            old_data = old._dict
            new_data = self._dict

            for field in old_data:
                old_value = old_data[field]
                new_value = new_data[field]

                if old_value != new_value:
                    field_obj = self._meta.get_field(field)

                    # If field is a ForeignKey, save the pk values instead of str
                    if isinstance(field_obj, models.ForeignKey):
                        old_value_repr = str(old_value.pk if old_value else '')
                        new_value_repr = str(new_value.pk if new_value else '')
                    else:
                        old_value_repr = str(old_value)
                        new_value_repr = str(new_value)

                    ChangeLog.objects.create(
                        field_name=field,
                        old_value=old_value_repr,
                        new_value=new_value_repr,
                        content_type=ContentType.objects.get_for_model(self),
                        object_id=self.pk,
                        changed_by=get_current_user()
                    )
        super().save(*args, **kwargs)

    @property
    def change_logs(self):
        return ChangeLog.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.pk
        )

    def field_change_logs(self, field_name):
        return self.change_logs.filter(field_name=field_name)

    def old_object(self, field_name):
        log = self.field_change_logs(field_name).first()
        if not log:
            return None
        field = self._meta.get_field(field_name)
        if isinstance(field, models.ForeignKey):
            model = field.remote_field.model
            try:
                return model.objects.get(pk=log.old_value)
            except model.DoesNotExist:
                return None
        return log.old_value

    def new_object(self, field_name):
        log = self.field_change_logs(field_name).first()
        if not log:
            return None
        field = self._meta.get_field(field_name)
        if isinstance(field, models.ForeignKey):
            model = field.remote_field.model
            try:
                return model.objects.get(pk=log.new_value)
            except model.DoesNotExist:
                return None
        return log.new_value