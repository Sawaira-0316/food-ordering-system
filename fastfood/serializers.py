from rest_framework import serializers
from .models import Order,Pizza,Burger


# post, get, delete, put
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['name', 'size','category','priceM', 'priceL', 'pImage']

class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = ['name', 'size', 'category', 'priceM', 'priceL', 'pImage']