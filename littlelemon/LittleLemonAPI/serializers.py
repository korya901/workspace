from django.contrib.auth.models import User
from rest_framework import serializers
from restaurant.models import *
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MenuItem
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']