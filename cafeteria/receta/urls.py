from django.urls import path, include
from . import views 
from rest_framework import routers

# Router para CRUD
router = routers.DefaultRouter()
router.register('recetas', views.RecetaView)
router.register('ingredientes', views.IngredienteView)
router.register('detallereceta', views.DetalleRecetaView)
#router.register('admin', views.AdminRecetaView)
#router.register('countreceta', views.CountIngredienteView)


urlpatterns = [
    path('',include(router.urls)),
    #Rutas para consultas, cantidad de ingredientes por receta
    path('count/', views.CountIngredienteView.as_view({'get': 'list'})),
    #Duracion de cada receta
    path('adminreceta/', views.AdminRecetaView.as_view({'get': 'list'})),
]
