from django.urls import path
from . import views

urlpatterns = [
    path('funcionarios/', views.funcionario_list, name='funcionario_list'),  # Lista de funcionários
    path('funcionarios/adicionar/', views.funcionario_create, name='funcionario_create'),  # Adicionar funcionário
    path('funcionarios/<int:pk>/editar/', views.funcionario_update, name='funcionario_update'),  # Editar funcionário
    path('funcionarios/<int:pk>/excluir/', views.funcionario_delete, name='funcionario_delete'),  # Excluir funcionário
    path('funcionarios/<int:pk>/', views.funcionario_detail, name='funcionario_detail'),  # Detalhes do funcionário
]
