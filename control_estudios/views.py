from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from control_estudios.models import Estudiante, Curso, Entregable, Profesor
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from control_estudios.forms import (
    CursoFormulario,
    ProfesorFormulario,
    EstudianteFormulario,
    EntregableFormulario,
)


def saludar_con_html(request):
    contexto = {"usuario": "Seba"}
    http_response = render(
        request=request,
        template_name="control_estudios/base.html",
        context=contexto,
    )
    return http_response


""" def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="control_estudios/listar_estudiantes.html",
        context=contexto,
    )
    return http_response
 """

def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="control_estudios/listar_cursos.html",
        context=contexto,
    )
    return http_response


def crear_cursos(request):
    if request.method == "POST":
        data = request.POST
        nombre = data["nombre"]
        comision = data["comision"]
        """ curso= Curso.objects.create(nombre=nombre, comision=comision) """
        curso = Curso(nombre=nombre, comision=comision)
        curso.save()
        url_exitosa = reverse("cursos")
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name="control_estudios/formulario_curso1.html",
        )
        return http_response


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(comision__contains=busqueda)
        contexto = {"cursos": cursos}

    http_response = render(
        request=request,
        template_name="control_estudios/listar_cursos.html",
        context=contexto,
    )
    return http_response


# FORMULARIOS


def crear_cursos2(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            comision = data["comision"]
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            url_exitosa = reverse("cursos")
            return redirect(url_exitosa)
        else:
            formulario = CursoFormulario(request.POST)

    else:
        formulario = CursoFormulario()
        http_response = render(
            request=request,
            template_name="control_estudios/formulario_curso2.html",
            context={"formulario": formulario},
        )
        return http_response


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse("cursos")
        return redirect(url_exitosa)


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data["nombre"]
            curso.comision = data["comision"]
            curso.descripcion = data["descripcion"]
            curso.save()
            url_exitosa = reverse("cursos")
        return redirect(url_exitosa)
    else: 
        inicial = {
            "nombre": curso.nombre,
            "comision": curso.comision,
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name="control_estudios/formulario_curso2.html",
        context={"formulario": formulario},
    )


def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            email = data["email"]
            telefono = data["telefono"]
            dni = data["dni"]
            fecha_nacimiento = data["fecha_nacimiento"]
            estudiante = Estudiante(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                dni=dni,
                fecha_nacimiento=fecha_nacimiento,
            )
            estudiante.save()
            url_exitosa = reverse("estudiantes")
            return redirect(url_exitosa)
        else:
            formulario = EstudianteFormulario(request.POST)

    else:
        formulario = EstudianteFormulario()
        http_response = render(
            request=request,
            template_name="control_estudios/formulario_estudiantes.html",
            context={"formulario": formulario},
        )
        return http_response


def crear_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            comision = data["comision"]
            profesor = Profesor(nombre=nombre, comision=comision)
            profesor.save()
            url_exitosa = reverse("cursos")
            return redirect(url_exitosa)
        else:
            formulario = ProfesorFormulario(request.POST)

    else:
        formulario = ProfesorFormulario()
        http_response = render(
            request=request,
            template_name="control_estudios/formulario_profesor.html",
            context={"formulario": formulario},
        )
        return http_response


def crear_entregable(request):
    if request.method == "POST":
        formulario = EntregableFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            fecha_entrega = data["fecha_entrega"]
            aprobado = data["aprobado"]
            entregable = Entregable(
                nombre=nombre, fecha_entrega=fecha_entrega, aprobado=aprobado
            )
            entregable.save()
            url_exitosa = reverse("cursos")
            return redirect(url_exitosa)
        else:
            formulario = EntregableFormulario(request.POST)

    else:
        formulario = EntregableFormulario()
        http_response = render(
            request=request,
            template_name="control_estudios/formulario_entregables.html",
            context={"formulario": formulario},
        )
        return http_response

#Vistas de estudiantes

class EstudianteListView(ListView):
    model = Estudiante
    template_name= "control_estudios/listar_estudiantes.html"
    
class EstudianteDetailView(DetailView):
    model = Estudiante
    """ success_url = reverse_lazy('listar_estudiantes') """
    
class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni')
    success_url = reverse_lazy('listar_estudiantes')
    
class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('listar_estudiantes')
    
class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('listar_estudiantes')