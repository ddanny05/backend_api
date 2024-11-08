from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all() #queryset permite hacer una consulta a los datos de mi modelo
    serializer_class = ClienteSerializer #serializer_class permite que los datos se serializen en un formato que pueda ser leído por otros sistemas
    permission_classes = [AllowAny] #permite que cualquier usuario pueda ver los datos, es decir, cualquiera puede acceder a los datos sin necesidad de estar logueado.
    