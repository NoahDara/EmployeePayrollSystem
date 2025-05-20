from django.contrib import admin
from .models import Currency, ExchangeRate
# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'symbol', 'country', 'is_active', )
    list_filter = ('is_active', 'is_base')
    search_fields = ('name', 'code',)
    date_hierarchy = 'updated'
    
@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('from_currency', 'to_currency', 'rate', 'effective_date')
    list_filter = ('from_currency', 'to_currency', 'effective_date')
    search_fields = ('to_currency',)
    date_hierarchy = 'updated'