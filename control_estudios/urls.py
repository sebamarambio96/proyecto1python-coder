from django.contrib import admin
from django.urls import path
from sistema_coder.views import saludar, saludar_con_html
from control_estudios.views import listar_estudiantes, listar_cursos

urlpatterns = [
    path("listarestu/", listar_estudiantes, name='estudiantes'),
    path("listarcursos/", listar_cursos, name='cursos'),
]
