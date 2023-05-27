from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from control_estudios.models import Noticias

def inicio(request):
    contexto = {
        "noticias": Noticias.objects.all(),
    }
    print(contexto)
    http_response = render(
        request=request,
        template_name="control_estudios/index.html",
        context=contexto,
    )
    return http_response

def saludar(request):
    saludo = "Hola"
    return HttpResponse(saludo)


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

