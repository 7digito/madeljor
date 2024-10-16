from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('apagar/<int:cliente_id>/', views.apagar_cliente, name='apagar_cliente'),
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('fornecedores/adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('fornecedores/editar/<str:id>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedores/apagar/<str:id>/', views.apagar_fornecedor, name='apagar_fornecedor'),
]
