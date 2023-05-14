from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True,max_length=64)
    comision = forms.IntegerField(required=True, max_value=50000)
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(required=True,max_length=64)
    apellido = forms.CharField(required=True, max_length=256)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True, max_length=20)
    dni = forms.CharField(required=True, max_length=50)
    fecha_nacimiento = forms.DateField()
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=True,max_length=64)
    comision = forms.IntegerField(required=True, max_value=50000)
    
class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    fecha_entrega = forms.DateTimeField(required=True)
    aprobado = forms.BooleanField(required=True)