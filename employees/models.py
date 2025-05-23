from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.SET_NULL, related_name='employee', null=True, blank=True)
    employee_number = models.CharField(max_length=50, unique=True)
    national_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[ ('male', 'Male'), ('female', 'Female'),('other', 'Other')])
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_number} - {self.first_name} {self.last_name}"