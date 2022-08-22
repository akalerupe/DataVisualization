from django.http import JsonResponse
from django.shortcuts import render
from .models import Order
from django.core import serializers


# Create your views here.
def dashboard_view(request):
    return render(request,"dashboard.html")

def pivot_data(request):
    dataset=Order.objects.all()
    data= serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


