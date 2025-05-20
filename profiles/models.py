from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    employee = models.OneToOneField("employees.Employee", on_delete=models.CASCADE)
    marital_status = models.ForeignKey("demographics.MaritalStatus", on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey("demographics.Race", on_delete=models.SET_NULL, null=True)
    disability_status = models.ForeignKey("demographics.DisabilityStatus", on_delete=models.SET_NULL, null=True)
    spoken_languages = models.ManyToManyField("demographics.Language")
    profile_picture = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Personal details for {self.employee}"
    
class ContactDetails(models.Model):
    employee = models.OneToOneField("employees.Employee", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact details for {self.employee}"
    
class NextOfKin(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.relationship}"

class EducationBackground(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    qualification = models.CharField(max_length=150)
    field_of_study = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    grade = models.CharField(max_length=50, choices=[ ('fail', 'Fail'),
        ('pass', 'Pass'), ('distinction', 'Distinction'), ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.qualification} at {self.institution}"
    
class WorkExperience(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    employer = models.CharField(max_length=200)
    position_held = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    reason_for_leaving = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.position_held} at {self.employer}"
