from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django_tables2 import RequestConfig

from .models import Trade, Asset, AssetAccount
from .forms import TradeForm
from .tables import TradeTable, AssetAccountTable
from .helper_functions import create_assetAccounts_afterTrade

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
    trades_table = TradeTable(trades)
   # RequestConfig(request).configure(trades_table)

    asset_account = AssetAccount.objects.filter(asset=asset)
    asset_account_table = AssetAccountTable(asset_account)
    RequestConfig(request).configure(asset_account_table)

    asset_account_buy = [x for x in asset_account if x.posting_type == "B"]
    asset_account_buy_table = AssetAccountTable(asset_account_buy)
    #RequestConfig(request).configure(asset_account_buy_table)

    asset_account_sell = [x for x in asset_account if x.posting_type == "S"]
    asset_account_sell_table = AssetAccountTable(asset_account_sell)
   # RequestConfig(request).configure(asset_account_sell_table)

    for table in [trades_table, asset_account_buy_table, asset_account_sell_table]:
        RequestConfig(request).configure(table)

    context = {'asset': asset,
               'trades_table': trades_table,
               'asset_account_table': asset_account_table,
               'asset_account_buy_table': asset_account_buy_table,
               'asset_account_sell_table': asset_account_sell_table,
               }
    return render(request, 'tracker/asset.html', context)



@require_http_methods(['POST'])
def createTrade(request):
    tradeForm = TradeForm(request.POST)

    if tradeForm.is_valid():
        if tradeForm.cleaned_data['asset_buy'] != tradeForm.cleaned_data['asset_sell']:
            date = tradeForm.cleaned_data['date']
            
            # Save the trade
            tradeForm.save()

            # Get the saved trade again
            trade = Trade.objects.get(date=date)

            # Create 3 (or 2 - without fees) entries of the effected AssetAccounts
            create_assetAccounts_afterTrade(trade)

            # Create 1 entry of the ProfitAccount, because of the sell position in the trade
                # if not fiat

    return redirect('/trades') #HttpResponseRedirect('')
