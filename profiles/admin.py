from django.contrib import admin
from .models import PersonalDetails, ContactDetails, NextOfKin, EducationBackground, WorkExperience
# Register your models here.
@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ('employee', 'marital_status', 'race', 'disability_status', 'created', )
    list_filter = ('marital_status', 'race', 'disability_status', 'created')
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__national_id')
    date_hierarchy = 'updated'
    
@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('employee', 'phone_number', 'email', 'address_line_1', 'address_line_2', 'city' )
    list_filter = ('created',)
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__national_id')
    date_hierarchy = 'updated'

@admin.register(NextOfKin)
class NextOfKinAdmin(admin.ModelAdmin):
    list_display = ('employee',  'first_name',  'last_name', 'relationship',  'contact_number',  'updated')
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__national_id', 'first_name', 'last_name')
    list_filter = ('updated',)
    date_hierarchy = 'updated'
    
@admin.register(EducationBackground)
class EducationBackgroundAdmin(admin.ModelAdmin):
    list_display = ('employee', 'institution', 'qualification', 'field_of_study', 'start_date', 'end_date' )
    list_filter = ('field_of_study', 'start_date',)
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__national_id',)
    date_hierarchy = 'updated'

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('employee',  'employer',  'position_held', 'start_date',  'end_date',  'updated')
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__national_id',)
    list_filter = ('created', 'updated', )
    date_hierarchy = 'updated'