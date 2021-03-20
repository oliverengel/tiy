from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns =[
    path('', views.index, name='index'),		                        #index -> dashboard
    path('trades', views.trades, name='trades'),	                    #overview of all trades, with filter
    path('assetSelection',views.assetSelection, name='assetSelection'), #User has to select on asset in order to enter the assetView
    path('asset/<str:asset_symbol>', views.asset, name='asset'),		#one asset: A) balance sheet, B) history of trades

    path('createTrade', views.createTrade, name='createTrade'),
]
