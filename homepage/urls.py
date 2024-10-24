# homepage/urls.py (ou seu arquivo de urls do projeto)
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # A homepage será acessível na raiz do site
]
