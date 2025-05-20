from django.contrib import admin
from .models import Company, Branch
# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_code', 'registration_number', 'tax_id', 'website', 'created')
    list_filter = ('created', 'industry',)
    search_fields = ('name', 'company_code', 'registration_number', 'tax_id',)
    date_hierarchy = 'updated'

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('company',  'name',  'code', 'address_line_1', 'address_line_2', 'city', 'phone_number',  'email')
    search_fields = ('name', 'code')
    list_filter = ('company', 'created',)
    date_hierarchy = 'updated'