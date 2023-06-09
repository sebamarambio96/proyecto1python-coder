from django.contrib import admin
from django.urls import path, include
from sistema_coder.views import inicio, sobre_mi
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', sobre_mi, name='sobre_mi'),
    path('admin/', admin.site.urls),
    path('plataforma/',include("control_estudios.urls")),
    path('accounts/',include("perfiles.urls")),
]

# Le agrega los archivos media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)