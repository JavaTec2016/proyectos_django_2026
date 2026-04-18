from django.db import models


# Create your models here.
class Alumno (models.Model):
    num_control = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=40)
    primer_ap = models.CharField(max_length=40)
    segundo_ap = models.CharField(max_length=40)
    fecha_nac = models.DateField()
    semestre = models.SmallIntegerField()
    carrera = models.CharField(max_length=100)
    
class Meta:
    db_table = 'alumnos'