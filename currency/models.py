from django.db import models
from django_countries.fields import CountryField
# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, blank=True)
    country = CountryField(blank=True)  # Replaces the CharField
    is_active = models.BooleanField(default=True)
    is_base = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.code} - {self.name}"
    
class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_rates')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_rates')
    rate = models.DecimalField(max_digits=20, decimal_places=6)
    effective_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('from_currency', 'to_currency', 'effective_date')
        ordering = ['-effective_date']

    def __str__(self):
        return f"1 {self.from_currency.code} = {self.rate} {self.to_currency.code} on {self.effective_date}"