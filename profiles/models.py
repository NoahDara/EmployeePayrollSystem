from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    employee = models.OneToOneField("employees.Employee", on_delete=models.CASCADE)
    marital_status = models.ForeignKey("demographics.MaritalStatus", on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey("demographics.Race", on_delete=models.SET_NULL, null=True)
    disability_status = models.ForeignKey("demographics.DisabilityStatus", on_delete=models.SET_NULL, null=True)
    number_of_children = models.PositiveIntegerField(default=0)
    spoken_languages = models.ManyToManyField("demographics.Language")
    profile_picture = models.ImageField(upload_to='employee_photos/', blank=True, null=True)

    def __str__(self):
        return f"Personal details for {self.employee}"
    
class Contact(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.CharField(max_length=50, choices=[
        ('mobile', 'Mobile'),
        ('email', 'Email'),
        ('home_phone', 'Home Phone'),
        ('work_phone', 'Work Phone'),
        ('emergency', 'Emergency Contact')
    ])
    value = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.contact_type} - {self.value}"
    
class NextOfKin(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.relationship}"

class EducationBackground(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    qualification = models.CharField(max_length=150)
    field_of_study = models.CharField(max_length=150)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=50, choices=[ ('fail', 'Fail'),
        ('pass', 'Pass'), ('distinction', 'Distinction'), ])
    
    def __str__(self):
        return f"{self.qualification} at {self.institution}"
    
class WorkExperience(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    employer = models.CharField(max_length=200)
    position_held = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    reason_for_leaving = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position_held} at {self.employer}"
