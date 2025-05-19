from django.db import models

# Create your models here.
class ContractType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Contract(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE, related_name='contracts')
    contract_type = models.ForeignKey(ContractType, on_delete=models.SET_NULL, null=True, related_name='contracts')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Contract For {self.employee}"