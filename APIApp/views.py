from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from models import User, Client, Address
from serializers import UserSerializer, ClientSerializer, AddressSerializer
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
     """
     API endpoint para visualizar e editar usuários.
     """
     queryset = User.objects.all()
     serializer_class = UserSerializer
     permission_classes = [permissions.IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
     """
     API endpoint para visualizar e editar nome dos clientes.
     """
     queryset = Client.objects.all()
     serializer_class = ClientSerializer
     permission_classes = [permissions.IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
     """
     API endpoint para visualizar e editar endereços.
     """
     queryset = Address.objects.all()
     serializer_class = AddressSerializer
     permission_classes = [permissions.IsAuthenticated]  

