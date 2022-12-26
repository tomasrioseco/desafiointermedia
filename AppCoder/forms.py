from django import forms

class CursoForm(forms.Form):
    nombre= forms.CharField(label="Nombre Curso", max_length=50)
    comision= forms.IntegerField(label="Comision")

class ProfeForm(forms.Form):
    nombre= forms.CharField(label="Nombre Profesor", max_length=50)
    apellido= forms.CharField(label="Apellido Profesor", max_length=50)
    email= forms.EmailField(label="Email Profesor")
    profesion= forms.CharField(label="Profesion Profesor", max_length=50)

class EstudianteForm(forms.Form):
    nombre= forms.CharField(label="Nombre Estudiante", max_length=50)
    apellido= forms.CharField(label="Apellido Estudiante", max_length=50)
    email= forms.EmailField(label="Email Estudiante")
    mat_aprobadas= forms.IntegerField(label="aprobadas Estudiante")

class EntregableForm(forms.Form):
    nombre= forms.CharField(label="Nombre Entregable", max_length=50)
    fecha_entrega= forms.DateField(label="fecha_entrega Entregable")
    entregado= forms.BooleanField(label="entregado Entregable")