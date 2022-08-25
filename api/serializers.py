from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):  
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields = "__all__"

    

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model=Stock
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    #product=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Order
        fields = "__all__"

    
