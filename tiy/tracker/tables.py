import django_tables2 as tables

from .models import Trade, AssetAccount

class TradeTable(tables.Table):
    class Meta:
        model = Trade
        exclude = {'id'}
        #template_name = 'django_tables2/bootstrap.html'
        #attrs = {"class": "myClassName"}


class AssetAccountTable(tables.Table):
    class Meta:
        model = AssetAccount
        exclude = {'id', 'trade', 'asset'}
        sequence = ('date', 'posting_type', 'asset_quantity', 'price', 'price_asset', 'open_quantity')