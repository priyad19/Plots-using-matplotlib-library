from rest_framework import serializers, validators
from .models import Addresses



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ("id", "user", "state", "district", "village","address1")