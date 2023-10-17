from rest_framework import viewsets
from . import serializers,models

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')


class PersonalViewSet(viewsets.ModelViewSet):
    queryset = models.Personal.objects.all()
    serializer_class = serializers.PersonalSerializaer


class clienteViewSet(viewsets.ModelViewSet):
    queryset = models.cliente.objects.all()
    serializer_class = serializers.clienteSerializaer

class facturasViewSet(viewsets.ModelViewSet):
    queryset = models.facturas.objects.all()
    serializer_class = serializers.facturasSerializaer

class usuariosViewSet(viewsets.ModelViewSet):
    queryset = models.usuarios.objects.all()
    serializer_class = serializers.usuariosSerializaer

class contratosViewSet(viewsets.ModelViewSet):
    queryset = models.contratos.objects.all()
    serializer_class = serializers.contratosSerializaer

