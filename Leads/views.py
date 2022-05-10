from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from . import models
from . import diferencia

def hola(request):
  return  HttpResponse("hola")

def AlumnosView(request):
  alumnos =  models.Alumno.objects.all().values()
  alumnos = list(alumnos)
  return  JsonResponse(alumnos, safe=False, json_dumps_params={'ensure_ascii':False})
  
def AlumnoView(request, pk):
  alumno =  models.Alumno.objects.get(pk=pk)
  return  JsonResponse(model_to_dict(alumno), safe=False, json_dumps_params={'ensure_ascii':False})
    
def MateriasView(request):
  materias =  models.Tecnicatura_en_Programación.objects.all().values()
  materias= list(materias)
  return  JsonResponse(materias, safe=False, json_dumps_params={'ensure_ascii':False})

def MateriaView(request, Materia):
  materia =  models.Tecnicatura_en_Programación.objects.get(Materia=Materia)
  return  JsonResponse(model_to_dict(materia), safe=False, json_dumps_params={'ensure_ascii':False})
  
def RegistroView(request, pk):

	if request.method =="POST":
		checkbox = str(request.POST.getlist('Materias'))
		print(checkbox)
		unwantedchar = "[]'"
		for char in unwantedchar:
			checkbox = checkbox.replace(char, "")
		alumno = models.Alumno.objects.get(id=pk)
		update = alumno.Materias_en_curso
		if update == "Ninguna":
				update = checkbox
		else:
			update = update + ", " + checkbox
		alumno.Materias_en_curso = update 
		alumno.save()
		nuevo_registro = models.Registro.objects.create(Alumno=alumno.id, Apellido = alumno.Apellido, Materia = checkbox)
		return  JsonResponse(model_to_dict(nuevo_registro), safe=False, json_dumps_params={'ensure_ascii':False})	
		
	elif request.method =="GET":
		Materias = list(models.Tecnicatura_en_Programación.objects.values_list('Materia', flat=True))
		Cursadas = models.Alumno.objects.get(id=pk).Materias_en_curso
		Cursadas = Cursadas.replace(" ", "")
		Cursadas = Cursadas.split(",")
		Diferencia = diferencia.diferencia(Materias, Cursadas)
		context = {
		'Materias': Materias,
		'Cursadas' : Cursadas,
		'Diferencia' : Diferencia
		}	
		print(Diferencia)
		return render (request, 'Index.html', context)
  
