from django.db import models

# Create your models here.
class Recetas(models.Model):
    name = models.CharField(max_length=30)
    duracion = models.PositiveIntegerField()
    preparacion = models.TextField()
    comentarios = models.TextField()

    def __str__(self):
        return self.name

class Ingrediente(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class DetalleReceta(models.Model):
    receta = models.ForeignKey(Recetas, on_delete= models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete= models.CASCADE)
    cantidad = models.PositiveIntegerField()
    MEDIDA = (('gr','gr'),('Taza','Taza'),('Mililitros','ml'),('Onza','oz'))
    medida = models.CharField(max_length=200, choices=MEDIDA)


    def __str__(self):
        return self.receta