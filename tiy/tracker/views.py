from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')


def trades(request):
    return HttpResponse('all trades as a list')


def asset(request):
    return HttpResponse('overview of one asset')
