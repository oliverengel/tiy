from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns =[
    path('', views.index, name='index'),		#index -> dashboard
    path('trades', views.trades, name='trades'),	#overview of all trades, with filter
    path('asset', views.asset, name='asset'),		#one asset: A) balance sheet, B) history of trades

#    path('addTrade', views.add_trade, name='add_trade'),
]
