from rest_framework import serializers
from ..models.cart import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'products']

