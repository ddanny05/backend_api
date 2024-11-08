from django.db import models


# Create your models here.
class Cliente (models.Model):
    cedula = models.CharField(max_length=10, primary_key=True) 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    def __str__(self):   #el metodo de devolucion se va a ejecutar siempre
            return f"{self.cedula}, {self.nombre}, {self.apellido }"