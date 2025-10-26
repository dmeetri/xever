from rest_framework import serializers
from .models import *

class PortfolioSerializer(serializers.ModelSerializer):
    video = serializers.FileField(use_url=True)
    
    class Meta:
        models = Portfolio
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    preview = serializers.ImageField(use_url=True)
    
    class Meta:
        models = Services
        fields = '__all__'