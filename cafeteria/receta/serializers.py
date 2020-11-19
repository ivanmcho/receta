from rest_framework import serializers
from .models import Recetas, Ingrediente, DetalleReceta

class RecetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recetas
        fields = ('id', 'url', 'name','duracion','preparacion','comentarios')

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'url','name')

class DetalleRecetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleReceta
        fields = ('id', 'url', 'receta','ingrediente','cantidad','medida')

class AdminRecetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recetas
        fields = ('id', 'url','name','duracion')

"""
class CountIngredienteSerializer(serializers.Serializer):
   
   receta = serializers.CharField(max_length=30)
   ingredientes = serializers.IntegerField()
   """