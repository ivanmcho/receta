from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('recetas', views.RecetaView)
router.register('ingredientes', views.IngredienteView)
router.register('detallereceta', views.DetalleRecetaView)
router.register('adminreceta', views.AdminRecetaView)


urlpatterns = [
    path('',include(router.urls)),
    #path('count/', views.CountIngredienteView.as_view()),
]
