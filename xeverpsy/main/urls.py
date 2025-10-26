from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('portfolio/', PortfolioList.as_view(), name='portfolio'),
    path('services/', ServicesList.as_view(), name='services'),
]