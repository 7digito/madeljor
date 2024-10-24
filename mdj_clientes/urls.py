from django.urls import path
from .views import cliente_list, cliente_create, cliente_update, cliente_delete

urlpatterns = [
    path('', cliente_list, name='cliente_list'),
    path('add/', cliente_create, name='cliente_create'),
    path('edit/<int:pk>/', cliente_update, name='cliente_update'),
    path('delete/<int:pk>/', cliente_delete, name='cliente_delete'),
]
