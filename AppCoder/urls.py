from django.urls import path
from .views import *



urlpatterns = [
    path("curso/", curso),
    path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path("", inicio, name="inicio"),

    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("profeFormulario/", profeFormulario, name="profeFormulario"),
    path("estudianteFormulario/", estudianteFormulario, name="estudianteFormulario"),
    path("entregableFormulario/", entregableFormulario, name="entregableFormulario"),

    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("busquedaProfesor/", busquedaProfesor, name="busquedaProfesor"),
    path("busquedaEstudiante/", busquedaEstudiante, name="busquedaEstudiante"),
    path("busquedaEntregable/", busquedaEntregable, name="busquedaEntregable"),
    
    path("buscarComision/", buscarComision, name="buscarComision"),
    path("buscarProfesor/", buscarProfesor, name="buscarProfesor"),
    path("buscarEstudiante/", buscarEstudiante, name="buscarEstudiante"),
    path("buscarEntregable/", buscarEntregable, name="buscarEntregable"),

]