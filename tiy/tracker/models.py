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



class AssetAccount(models.Model):
    POSTING_TYPES = [
        ('B','Buy'),
        ('F','Fee'),
        ('S','Sell'),
    ]

    date = models.DateTimeField()
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='account_asset', verbose_name='asset')
    asset_quantity = models.DecimalField(max_digits=14, decimal_places=8, verbose_name='quantity')
    price = models.DecimalField(max_digits=14, decimal_places=8)
    posting_type = models.CharField(max_length=1, choices=POSTING_TYPES)
    open_quantity = models.DecimalField(max_digits=14, decimal_places=8, verbose_name='open')

    def __str__(self):
       # return self.date + ": " + self.posting_type + " " + self.asset
        return self.date + ': %s %s' %(self.posting_type, self.asset)



class Broker(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Exchange(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class ProfitAccount(models.Model):
    date = models.DateTimeField()
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='account_asset', verbose_name='asset')
   # profit_in_asset_fifo
   # profit_in_asset_percentage_fifo
   # profit_in_euro_fifo
   # profit_in_asset_avg
   # profit_in_asset_percentage_avg
   # profit_in_euro_avg
   # price_asset_euro #exchange rate to fiat

    def __str__(self):
        return self.date + ': Profit booked for %s.' %self.asset



class Trade(models.Model):
    date = models.DateTimeField()

    asset_buy = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='asset_buy', verbose_name='buy')
    asset_buy_quantity = models.DecimalField(max_digits=14, decimal_places=8, verbose_name='buy quantity')

    asset_sell = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='asset_sell', verbose_name='sell')
    asset_sell_quantity = models.DecimalField(max_digits=14, decimal_places=8, verbose_name='sell quantity')

    fee = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name='fee')
    fee_quantity = models.DecimalField(max_digits=14, decimal_places=8)

    broker = models.ForeignKey(Broker, on_delete=models.PROTECT, related_name='broker')
    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT, related_name='exchange')
    note = models.TextField(blank=True)

    def __str__(self):
        return "On " + str(self.date) + ": Bought " + str(self.asset_buy_quantity) + " " + str(self.asset_buy.symbol) + "."


