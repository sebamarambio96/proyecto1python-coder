from django.shortcuts import render, redirect
from django.urls import reverse
from control_estudios.models import Estudiante, Curso
from control_estudios.forms import CursoFormulario


def saludar_con_html(request):
    contexto = {"usuario": "Seba"}
    http_response = render(
        request=request,
        template_name="control_estudios/base.html",
        context=contexto,
    )
    return http_response


def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="control_estudios/listar_estudiantes.html",
        context=contexto,
    )
    return http_response


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
            context={'formulario': formulario}
        )
        return http_response
