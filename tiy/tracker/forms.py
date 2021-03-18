from django.forms import ModelForm, SelectDateWidget
from django.forms.widgets import DateTimeInput
import datetime

from .models import Trade


class TradeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TradeForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.datetime.now()
        self.fields['asset_buy'].queryset = self.fields['asset_buy'].queryset.order_by('symbol')
        self.fields['asset_sell'].queryset = self.fields['asset_sell'].queryset.order_by('symbol')
        self.fields['fee'].queryset = self.fields['fee'].queryset.order_by('symbol')

    class Meta:
        model = Trade
        fields = '__all__'

