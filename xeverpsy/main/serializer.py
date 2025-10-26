from rest_framework import serializers
from .models import Portfolio, Services

class PortfolioSerializer(serializers.ModelSerializer):
    video = serializers.FileField(use_url=True)

    class Meta:
        model = Portfolio
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    preview = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Services
        fields = '__all__'