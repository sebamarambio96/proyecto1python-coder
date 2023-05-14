from django.contrib import admin
from django.urls import path
from sistema_coder.views import saludar, saludar_con_html
from control_estudios.views import listar_estudiantes, listar_cursos, crear_cursos, crear_cursos2, buscar_cursos,\
    crear_estudiante, crear_profesor, crear_entregable

urlpatterns = [
    path("listarestu/", listar_estudiantes, name='estudiantes'),
    path("listarcursos/", listar_cursos, name='cursos'),
    path("crear-cursos/", crear_cursos, name='crear_cursos_1'),
    path("buscar-cursos/", buscar_cursos, name='buscar_cursos'),
    #FORMULARIOS
    path("crear-cursos2/", crear_cursos2, name='crear_cursos_2'),
    path("crear-estudiante/", crear_estudiante, name='crear_estudiante'),
    path("crear-profesor/", crear_profesor, name='crear_profesor'),
    path("crear-entregable/", crear_entregable, name='crear_entregable'),
]
