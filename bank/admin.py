from django.contrib import admin
from .models import BankAccount
# Register your models here.
@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('owner', 'account_holder', 'account_number', 'bank_name', 'account_type', 'currency', 'is_primary', 'is_active')
    list_filter = ('account_type', 'currency', 'is_primary')
    search_fields = ('account_holder', 'bank_name')
    date_hierarchy = 'updated'