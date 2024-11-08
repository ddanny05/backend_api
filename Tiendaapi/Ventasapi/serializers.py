from rest_framework import serializers 
from .models import Cliente

#un serializador convierte los diricionarios de python (registros) en archuvos formato json (formato de una api)
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('cedula', 'nombre', 'apellido', 'telefono', 'correo')  #los campos que quiero que aparezcan en el json
        