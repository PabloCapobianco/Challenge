from django.urls import path, include
from . import views


urlpatterns = [

    path('alumnos', views.AlumnosView),
    path('alumno/<int:pk>/', views.AlumnoView),
    path('materias', views.MateriasView),
    path('materia/<str:Materia>/', views.MateriaView),
    path('registro/<int:pk>/', views.RegistroView),
]
