from rest_framework import serializers
from .models import Shoe, User

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ['id', 'title', 'description', 'price', 'old_price', 'brand', 'material', 'color', 'size', 'stock', 'image', 'image2', 'image3', 'image4', 'rating', 'createdAt', 'gender', 'onSale', 'discountPercent', 'newCollection', 'season']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'permission_level', 'favorite_shoes']
