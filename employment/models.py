from django.db import models

# Create your models here.
class Employment(models.Model):
    employee = models.OneToOneField("employees.Employee", on_delete=models.CASCADE, related_name='employment')
    job_title = models.ForeignKey("positions.JobTitle", on_delete=models.SET_NULL, null=True, related_name='employments')
    company = models.ForeignKey("organization.Branch", on_delete=models.SET_NULL, null=True, related_name='employments')
    branch = models.ForeignKey("organization.Branch", on_delete=models.SET_NULL, null=True, related_name='employments')
    department = models.ForeignKey("divisions.Department", on_delete=models.SET_NULL, null=True, related_name='employments')
    section = models.ForeignKey("divisions.Section", on_delete=models.SET_NULL, null=True, blank=True, related_name='employments')
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
    
class Promotion(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    old_job_title = models.ForeignKey("positions.JobTitle", on_delete=models.SET_NULL, null=True, related_name='previous_titles')
    new_job_title = models.ForeignKey("positions.JobTitle", on_delete=models.SET_NULL, null=True, related_name='promoted_titles')
    promotion_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employment.employee} promoted to {self.new_job_title}"
    
class Transfer(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    from_branch = models.ForeignKey("organizations.Branch", on_delete=models.SET_NULL, null=True, related_name='transfer_from')
    to_branch = models.ForeignKey("organizations.Branch", on_delete=models.SET_NULL, null=True, related_name='transfer_to')
    transfer_date = models.DateField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employment.employee} transfer to {self.to_department or self.to_branch}"
    
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

    def __str__(self):
        return f"{self.employment.employee} exited via {self.exit_type}"