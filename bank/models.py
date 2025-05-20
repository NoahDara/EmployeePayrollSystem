from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class BankAccount(models.Model):
    account_holder = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=30, choices=[
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('other', 'Other')
    ])
    currency =  models.ForeignKey("currency.Currency", on_delete=models.CASCADE, related_name='banks')

    # Generic relation for reusability
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    owner = GenericForeignKey('content_type', 'object_id')

    is_primary = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.is_primary:
            # Unset other primary accounts for the same owner
            BankAccount.objects.filter(
                content_type=self.content_type,
                object_id=self.object_id,
                is_primary=True
            ).exclude(pk=self.pk).update(is_primary=False)

    def __str__(self):
        return f"{self.account_holder} - {self.account_number}"