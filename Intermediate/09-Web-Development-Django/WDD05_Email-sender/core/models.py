from django.db import models

class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    
    def __str__(self):
        return self.nombre