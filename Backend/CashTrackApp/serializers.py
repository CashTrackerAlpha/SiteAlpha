# serializers.py
from rest_framework import serializers
from .models.AccountModel import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__' 
