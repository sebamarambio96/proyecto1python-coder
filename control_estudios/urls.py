from django.contrib import admin
from django.urls import path
from sistema_coder.views import saludar, saludar_con_html
from control_estudios.views import listar_estudiantes, listar_cursos, crear_cursos, crear_cursos2

urlpatterns = [
    path("listarestu/", listar_estudiantes, name='estudiantes'),
    path("listarcursos/", listar_cursos, name='cursos'),
    path("crear-cursos/", crear_cursos, name='crear_cursos_1'),
    path("crear-cursos2/", crear_cursos2, name='crear_cursos_2'),
]
