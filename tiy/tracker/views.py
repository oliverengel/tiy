from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Trade
from .forms import TradeForm

# Create your views here.
def index(request):
    tradeForm = TradeForm()
    context = {'tradeForm': tradeForm}
    return render(request, 'tracker/index.html', context)



def trades(request):
    tradeForm = TradeForm()
    trades = Trade.objects.all()
    context = {'tradeForm': tradeForm, 'trades': trades}
    return render(request, 'tracker/trades.html', context)



def asset(request):
    return HttpResponse('overview of one asset')



@require_http_methods(['POST'])
def createTrade(request):
    tradeForm = TradeForm(request.POST)

    if tradeForm.is_valid():
        tradeForm.save()

    return redirect('/')
