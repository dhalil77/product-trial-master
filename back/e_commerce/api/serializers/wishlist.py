from rest_framework import serializers
from ..models.wishlist import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'products']
