from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from .models import Recetas, Ingrediente, DetalleReceta
from .serializers import RecetaSerializer, IngredienteSerializer, DetalleRecetaSerializer, AdminRecetaSerializer, CountSerializer

# En settings esta configurado para denegar el acceso, siempre que no este autenticado 
# CRUD de receta, ingrediente y detalle
class RecetaView(viewsets.ModelViewSet):
    queryset = Recetas.objects.all()
    serializer_class = RecetaSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class IngredienteView(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class DetalleRecetaView(viewsets.ModelViewSet):
    queryset = DetalleReceta.objects.all()
    serializer_class = DetalleRecetaSerializer

# Duracion es un campo de receta, por lo que solo llamamos esos campos
class AdminRecetaView(viewsets.ModelViewSet):
    queryset = Recetas.objects.only('id', 'name','duracion')
    serializer_class = AdminRecetaSerializer

# Se hace un queryset contando los ingredientes que tiene cada receta
class CountIngredienteView(viewsets.ModelViewSet):
    queryset = Recetas.objects.annotate(recuentoIngrediente=Count('detallereceta'))
    serializer_class = CountSerializer