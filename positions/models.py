from django.db import models

# Create your models here.
class JobGrade(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    minimum_salary = models.DecimalField(max_digits=20, decimal_places=2)
    maximum_salary = models.DecimalField(max_digits=20, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class JobTitle(models.Model):
    job_grade = models.ForeignKey(JobGrade, on_delete=models.SET_NULL, null=True, related_name='job_titles')
    title = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    is_supervisory = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
