from django.urls import path
from .views import cliente_list, cliente_create, cliente_update, cliente_delete

urlpatterns = [
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/adicionar/', cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/deletar/', cliente_delete, name='cliente_delete'),
]
