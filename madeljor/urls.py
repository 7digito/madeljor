from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # Inclua as URLs da app homepage
    path('clientes/', include('mdj_clientes.urls')),  # Inclui as URLs da app de clientes
    path('fornecedores/', include('fornecedores.urls')),  # Inclui as URLs da app de fornecedores
    path('funcionarios/', include('funcionarios.urls')),  # Inclui as URLs da app de funcionários
]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
