from django.urls import path
from control_estudios.views import NoticiasDetailView,NoticiasListView,NoticiasUpdateView,NoticiasDeleteView, MisNoticiasListView
urlpatterns = [
    #NOTICIAS
    path('pages/<int:pk>/', NoticiasDetailView.as_view(), name="ver_noticia"),
    path('pages/', NoticiasListView.as_view(), name="listar_noticias"),
    path('mis-noticias/', MisNoticiasListView.as_view(), name="mis_noticias"),
    path('editar-noticia/<int:pk>/', NoticiasUpdateView.as_view(), name="editar_noticia"),
    path('eliminar-noticia/<int:pk>/', NoticiasDeleteView.as_view(), name="eliminar_noticia"),
]
