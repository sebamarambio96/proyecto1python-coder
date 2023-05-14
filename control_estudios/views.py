from django.shortcuts import render

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
        "estudiantes":[
            {"nombre":"Seba", "apellido":"Marambio"},
            {"nombre":"cami", "apellido":"Marambio"},
            {"nombre":"felipe", "apellido":"Marambio"},
            {"nombre":"Zhinus", "apellido":"Manshadi"},
            ]
    }
    http_response = render(
        request=request,
        template_name="control_estudios/listar_estudiantes.html",
        context=contexto,
    )
    return http_response

def listar_cursos(request):
    contexto = {
        "cursos":[
            {"nombre":"Python", "comision":"1234"},
            {"nombre":"AWS", "comision":"1324234"},
            ]
    }
    http_response = render(
        request=request,
        template_name="control_estudios/listar_cursos.html",
        context=contexto,
    )
    return http_response

