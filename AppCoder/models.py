from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre= models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {str(self.comision)}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    mat_aprobadas=models.IntegerField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()