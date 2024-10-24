from django.urls import path
from .views import fornecedor_list, fornecedor_create, fornecedor_update, fornecedor_delete

urlpatterns = [
    path('', fornecedor_list, name='fornecedor_list'),  # Exemplo de URL para listar fornecedores
    path('create/', fornecedor_create, name='fornecedor_create'),
    path('update/<int:pk>/', fornecedor_update, name='fornecedor_update'),
    path('delete/<int:pk>/', fornecedor_delete, name='fornecedor_delete'),
]
