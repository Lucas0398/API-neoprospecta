from rest_framework import serializers
from models import User, Client, Address

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserName','client','mainaddress','address']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['ClientName']

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ['rua','cidade','estado','CEP','pais']
    