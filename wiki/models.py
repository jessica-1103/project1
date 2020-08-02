from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=50, default='')
    descripcion = models.TextField(blank=True, default='')
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return self.titulo


class Autor(models.Model):
    nombre = models.CharField(max_length=50, default='')
    edad = models.IntegerField(blank=True)
      
      
    def __str__(self):
            return self.nombre

