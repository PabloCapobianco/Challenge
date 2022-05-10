from django.db import models

class Tecnicatura_en_Programación(models.Model):
	Materia = models.CharField(max_length=100)
	Alumnos_inscriptos = models.CharField(max_length=100, default = "Ninguno")	
	Horas_semanales = models.PositiveIntegerField(null =True) 


class Alumno(models.Model):
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	DNI = models.CharField(max_length=100)
	Email = models.EmailField(max_length=100)
	Materias_en_curso = models.CharField(max_length=200, default = "Ninguna")

class Registro(models.Model):
	Alumno= models.PositiveIntegerField()
	Apellido = models.CharField(max_length=100)
	Materia = models.CharField(max_length=100)
	Fecha = models.DateTimeField(auto_now_add=True)
	
	
	
	
	
