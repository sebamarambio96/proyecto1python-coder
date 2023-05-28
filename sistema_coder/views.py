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
