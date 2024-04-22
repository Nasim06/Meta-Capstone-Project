from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        