from rest_framework import serializers
from . import models

class PersonalSerializaer(serializers.ModelSerializer):
    class Meta:
        model = models.Personal
        fields = "__all__"

#------------------------------------------------------------

class clienteSerializaer(serializers.ModelSerializer):
    fecha = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S",
        input_formats=(['%d/%m/%Y %H:%M:%S','iso-8601']))
    class Meta:
        model = models.cliente
        fields = "__all__"


class facturasSerializaer(serializers.ModelSerializer):
    fecha = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S",
        input_formats=(['%d/%m/%Y %H:%M:%S','iso-8601']))
    class Meta:
        model = models.facturas
        fields = "__all__"

class usuariosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = models.usuarios
        fields = "__all__"

class contratosSerializaer(serializers.ModelSerializer):
    class Meta:
        model = models.contratos
        fields = "__all__"