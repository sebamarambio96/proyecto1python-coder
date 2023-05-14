from django.shortcuts import render

from control_estudios.models import Estudiante, Curso


def saludar_con_html(request):
    contexto = {
        "usuario":"Seba"
    }
    http_response = render(
        request=request,
        template_name="control_estudios/base.html",
        context=contexto,
    )
    return http_response

def listar_estudiantes(request):
    contexto = {
        "estudiantes":Estudiante.objects.all(),
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

