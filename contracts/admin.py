from django.contrib import admin
from .models import ContractType, Contract
# Register your models here.
@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'created')
    list_filter = ('is_active', 'updated')
    search_fields = ('name', 'code',)
    date_hierarchy = 'updated'
    
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('employee', 'contract_type', 'start_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'contract_type')
    search_fields = ('employee',)
    date_hierarchy = 'updated'