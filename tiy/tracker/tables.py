import django_tables2 as tables

from .models import Trade

class TradeTable(tables.Table):
    class Meta:
        model = Trade
        exclude = {'id', 'note'}
        #template_name = 'django_tables2/bootstrap.html'
        #attrs = {"class": "myClassName"}
