from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recetas, Ingrediente, DetalleReceta
from .serializers import RecetaSerializer, IngredienteSerializer, DetalleRecetaSerializer, AdminRecetaSerializer



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

class AdminRecetaView(viewsets.ModelViewSet):
    queryset = Recetas.objects.only('id', 'name','duracion')
    serializer_class = AdminRecetaSerializer

""""
class CountIngredienteView(APIView):

    def get(self, request):
        yourdata= DetalleReceta.objects.values('receta').count()
        results = CountIngredienteSerializer(yourdata, many=True).data
        return Response(results)"""