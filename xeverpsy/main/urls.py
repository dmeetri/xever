from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('works/', works, name='works'),
    path('watch/<int:video_id>/', video_detail, name='video_detail')
]