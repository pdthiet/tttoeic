from rest_framework import serializers
from .models import *

class GetAllVipPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VipPrice
        fields = '__all__'

class GetAllVipFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VipFunction
        fields = '__all__'

class UpdateVipPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VipPrice
        fields = ['month', 'price', 'sale_price']

class CreateVipPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VipPrice
        fields = ['month', 'price', 'sale_price']