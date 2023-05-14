from django.contrib import admin
from django.urls import path, include
from sistema_coder.views import saludar,saludar_con_html, inicio
from control_estudios.views import listar_estudiantes, listar_cursos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('saludo/', saludar),
    path('saludohtml/', saludar_con_html),
    path('plataforma/',include("control_estudios.urls")),
]
