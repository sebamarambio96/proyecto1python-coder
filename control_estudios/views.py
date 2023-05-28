from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from control_estudios.models import Noticias
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
    
#NOTICIAS
@login_required
def crear_noticia(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        titular = data["titular"]
        subtitulo = data["subtitulo"]
        cuerpo = data["cuerpo"]
        categoria = data["categoria"]
        portada_img = request.FILES.get("portada_img")
        autor = request.user
        noticias = Noticias(titular=titular, subtitulo=subtitulo, cuerpo=cuerpo, categoria=categoria, autor=autor, imagen=portada_img)
        noticias.save()
        url_exitosa = reverse("mis_noticias")
        return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name="control_estudios/formulario_noticia.html",
        )
        return http_response


class NoticiasDetailView(DetailView):
    model = Noticias
    
class MisNoticiasListView(LoginRequiredMixin, ListView):
    model = Noticias
    template_name= "control_estudios/mis_noticias.html"

class NoticiasListView(ListView):
    model = Noticias
    template_name= "control_estudios/listar_noticias.html"
    
class NoticiasUpdateView(LoginRequiredMixin, UpdateView):
    model = Noticias
    fields = ('titular', 'subtitulo', 'categoria', 'cuerpo', 'imagen')
    success_url = reverse_lazy('mis_noticias')   
    
class NoticiasDeleteView(LoginRequiredMixin, DeleteView):
    model = Noticias
    success_url = reverse_lazy('mis_noticias')
    
    