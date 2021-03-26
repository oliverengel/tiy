from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig

from .models import Trade, Asset
from .forms import TradeForm
from .tables import TradeTable

# Create your views here.
def index(request):	#Dashboard
    tradeForm = TradeForm()
    context = {'tradeForm': tradeForm}
    return render(request, 'tracker/index.html', context)



def trades(request):
    tradeForm = TradeForm()
    trades = Trade.objects.all()
    table = TradeTable(trades)
    RequestConfig(request).configure(table)
    context = {'tradeForm': tradeForm, 'table': table}
    return render(request, 'tracker/trades.html', context)



def assetSelection(request):
    assets = Asset.objects.all().order_by('symbol')
    asset_types = dict(Asset.ASSET_TYPES)
    used_types_set = {x.type for x in assets}                           #Gets all used assetTypes from the db as set
    used_types_dict = {x: asset_types[x] for x in used_types_set}       #Converts all used assetTypes into a dict
    context = {'assets': assets, 'used_types': used_types_dict}
    return render(request, 'tracker/asset_selection.html', context)


def asset(request, asset_symbol):
    asset = Asset.objects.get(symbol=asset_symbol)
    trades = Trade.objects.filter(asset_buy=asset) | Trade.objects.filter(asset_sell=asset)
    table = TradeTable(trades)
    RequestConfig(request).configure(table)
    context = {'table': table}
    return render(request, 'tracker/asset.html', context)



@require_http_methods(['POST'])
def createTrade(request):
    tradeForm = TradeForm(request.POST)

    if tradeForm.is_valid():
        if tradeForm.cleaned_data['asset_buy'] != tradeForm.cleaned_data['asset_sell']:
            tradeForm.save()

    return redirect('/trades') #HttpResponseRedirect('')
