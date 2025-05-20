from django.db import models

# Create your models here.
class Employment(models.Model):
    employee = models.OneToOneField("employees.Employee", on_delete=models.CASCADE, related_name='employment')
    job_title = models.ForeignKey("positions.JobTitle", on_delete=models.SET_NULL, null=True, related_name='employments')
    job_grade = models.ForeignKey("positions.JobGrade", on_delete=models.SET_NULL, null=True, related_name='employments')
    company = models.ForeignKey("organization.Company", on_delete=models.SET_NULL, null=True, related_name='employments')
    branch = models.ForeignKey("organization.Branch", on_delete=models.SET_NULL, null=True, related_name='employments')
    engagement_date = models.DateField()
    supervisor = models.ForeignKey("self", related_name='subordinates',on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=30,
        choices=[('active', 'Active'), ('suspended', 'Suspended'), ('terminated', 'Terminated'), ('resigned', 'Resigned')],
        default='active')
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.job_title}"
    
class Exit(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    exit_type = models.CharField(max_length=30, choices=[
        ('resignation', 'Resignation'),
        ('retirement', 'Retirement'),
        ('termination', 'Termination'),
    ])
    exit_date = models.DateField()
    reason = models.TextField(blank=True)
    is_finalized = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employment.employee} exited via {self.exit_type}"