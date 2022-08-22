import imp
from django.urls import path
from .views import dashboard_view,pivot_data

urlpatterns = [
   path('',dashboard_view,name="dashboard_view"),
   path('data/',pivot_data,name="pivot_data"),

 
]
