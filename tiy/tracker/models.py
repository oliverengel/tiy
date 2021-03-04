from django.db import models

# Create your models here.
class Trade(models.Model):
    date = models.DateField()
    asset_buy = models.CharField(max_length=3)
    asset_buy_quantity = models.DecimalField(max_digits=12, decimal_places=8)
    asset_sell = models.CharField(max_length=3)
    asset_sell_quantity = models.DecimalField(max_digits=12, decimal_places=8)
    fee_in_asset = models.CharField(max_length=3)
    fee_quantity = models.DecimalField(max_digits=12, decimal_places=8)
    broker = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __str__(self):
        return "On " + self.date + " bought " + self.asset_buy + "."
