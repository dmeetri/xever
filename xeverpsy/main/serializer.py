from rest_framework import serializers
from .models import *

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        models = Portfolio
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Services
        fields = '__all__'