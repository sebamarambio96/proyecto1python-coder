from django.contrib import admin
from django.urls import path
from sistema_coder.views import saludar, saludar_con_html
from control_estudios.views import listar_cursos, crear_cursos2, buscar_cursos,\
     crear_profesor, crear_entregable, eliminar_curso, editar_curso, EstudianteListView, EstudianteCreateView,\
    EstudianteDetailView, EstudianteUpdateView, EstudianteDeleteView,crear_noticia,NoticiasDetailView,NoticiasListView
urlpatterns = [
    #CURSOS
    path("listarcursos/", listar_cursos, name='cursos'),
    path("crear-noticia/", crear_noticia, name='crear_noticia'),
    path("buscar-cursos/", buscar_cursos, name='buscar_cursos'),
    #FORMULARIOS
    path("crear-cursos2/", crear_cursos2, name='crear_cursos_2'),
    path("crear-profesor/", crear_profesor, name='crear_profesor'),
    path("crear-entregable/", crear_entregable, name='crear_entregable'),
    path("eliminar-curso/<int:id>/", eliminar_curso, name="eliminar_curso"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
    #ESTUDIANTES
    path("estudiantes/", EstudianteListView.as_view(), name='listar_estudiantes'),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
    path('crear-estudiante/', EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-estudiante/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-estudiante/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
    #NOTICIAS
    path('noticia/<int:pk>/', NoticiasDetailView.as_view(), name="ver_noticia"),
    path('mis-noticias/', NoticiasListView.as_view(), name="mis_noticias"),
]
