from django.db import models

# Create your models here.
class Asset(models.Model):
    ASSET_TYPES = [
        ('CO','Commodity'),
        ('CR','Crypto'),
        ('FI','Fiat'),
        ('FU','Fund'),
        ('ST','Stock'),
    ]

    name = models.CharField(max_length=15)
    symbol = models.CharField(max_length=5)
    type = models.CharField(max_length=2, choices=ASSET_TYPES)

    def __str__(self):
        return self.symbol



class Broker(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Exchange(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Trade(models.Model):

    date = models.DateTimeField()

    asset_buy = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='asset_buy')
    asset_buy_quantity = models.DecimalField(max_digits=14, decimal_places=8)

    asset_sell = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='asset_sell')
    asset_sell_quantity = models.DecimalField(max_digits=14, decimal_places=8)

    fee = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='fee')
    fee_quantity = models.DecimalField(max_digits=14, decimal_places=8)

    broker = models.ForeignKey(Broker, on_delete=models.PROTECT, related_name='broker')
    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT, related_name='exchange')
    note = models.TextField(blank=True)

    def __str__(self):
        return "On " + str(self.date) + ": Bought " + str(self.asset_buy_quantity) + " " + str(self.asset_buy.symbol) + "."


'''
class TradeResult(models.Model): #Profit
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    profit = models.DecimalField(max_digits=14, decimal_places=8)
    currency = models.ForeignKey(Asset, on_delete=models.PROETCT, related_name='profit_currency')
'''
