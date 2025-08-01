from django.db import models

# Create your models here.

class Libro(models.Model):
    Autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('prestado', 'Prestado')], default='disponible')

    def __str__(self):
        return super().__str__()