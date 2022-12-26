from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from AppCoder.forms import *
# Create your views here.

def curso(request):

    cursito= Curso(nombre="JavaScript", comision=123456)
    cursito.save()
    cadena_texto=f"curso guardado: Nombre: {cursito.nombre}, Comision: {cursito.comision}"
    return HttpResponse(cadena_texto)


def cursos(request):
    return render (request, "AppCoder/cursos.html")

def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")

def profesores(request):
    return render (request, "AppCoder/profesores.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")

def inicio(request):
    return render (request, "AppCoder/inicio.html")

""" def cursoFormulario(request):
    if request.method=="POST":
        nombre= request.POST["nombre"]
        comision= request.POST["comision"]
        print(nombre, comision)
        curso= Curso(nombre=nombre, comision=comision)
        curso.save()
        return render(request, "AppCoder/inicio.html" ,{"mensaje": "Curso guardado correctamente"})
        
    else:
        return render (request, "AppCoder/cursoFormulario.html") """


def cursoFormulario(request):
    if request.method=="POST":
        form= CursoForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            print(informacion)
            nombre= informacion["nombre"]
            comision= informacion["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Curso guardado correctamente"})
        else:
            return render(request, "AppCoder/cursoFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= CursoForm()
        return render (request, "AppCoder/cursoFormulario.html", {"form": formulario})

def profeFormulario(request):
    if request.method=="POST":
        form= ProfeForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            profesion= informacion["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Profesor guardado correctamente"})
        else:
            return render(request, "AppCoder/ProfeFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= ProfeForm()
        return render (request, "AppCoder/ProfeFormulario.html", {"form": formulario})

def estudianteFormulario(request):
    if request.method=="POST":
        form= EstudianteForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            mat_aprobadas= informacion["mat_aprobadas"]
            estudiante= Estudiante(nombre=nombre, apellido=apellido, email=email, mat_aprobadas=mat_aprobadas)
            estudiante.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Estudiante guardado correctamente"})
        else:
            return render(request, "AppCoder/estudianteFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= EstudianteForm()
        return render (request, "AppCoder/estudianteFormulario.html", {"form": formulario})

def entregableFormulario(request):
    if request.method=="POST":
        form= EntregableForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            fecha_entrega= informacion["fecha_entrega"]
            entregado= informacion["entregado"]
            entregable= Entregable(nombre=nombre, fecha_entrega=fecha_entrega, entregado=entregado)
            entregable.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Entregable guardada correctamente"})
        else:
            return render(request, "AppCoder/entregableFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= EntregableForm()
        return render (request, "AppCoder/entregableFormulario.html", {"form": formulario})

def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def busquedaProfesor(request):
    return render(request, "AppCoder/busquedaProfesor.html")

def busquedaEstudiante(request):
    return render(request, "AppCoder/busquedaEstudiante.html")

def busquedaEntregable(request):
    return render(request, "AppCoder/busquedaEntregable.html")

def buscarComision(request):
    
    comision= request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__icontains=comision)#buscar otros filtros en la documentacion de django
        return render(request, "AppCoder/resultadosBusquedaComision.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Che Ingresa una comision para buscar!"})

def buscarProfesor(request):

    profesor= request.GET["nombre"]
    if profesor!="":
        profes= Profesor.objects.filter(nombre__icontains=profesor)
        return render(request, "AppCoder/resultadosBusquedaProfesor.html", {"profes": profes})
    else:
        return render(request, "AppCoder/busquedaProfesor.html", {"mensaje": "Che Ingresa un profesor para buscar!"})

def buscarEstudiante(request):
    
    estudiante= request.GET["nombre"]
    if estudiante!="":
        estudiantes= Estudiante.objects.filter(nombre__icontains=estudiante)
        return render(request, "AppCoder/resultadosBusquedaEstudiante.html", {"estudiantes": estudiantes})
    else:
        return render(request, "AppCoder/busquedaEstudiante.html", {"mensaje": "Che Ingresa un estudiante para buscar!"})

def buscarEntregable(request):
    
    entregable= request.GET["nombre"]
    if entregable!="":
        entregables= Entregable.objects.filter(nombre__icontains=entregable)
        return render(request, "AppCoder/resultadosBusquedaEntregable.html", {"entregables": entregables})
    else:
        return render(request, "AppCoder/busquedaEntregables.html", {"mensaje": "Che Ingresa un entregable para buscar!"})
