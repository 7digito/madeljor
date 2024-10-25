from django.urls import path
from .views import ObraListView, ObraDetailView, ObraCreateView, ObraUpdateView, ObraDeleteView

urlpatterns = [
    path('', ObraListView.as_view(), name='obra_list'),
    path('obra/<int:pk>/', ObraDetailView.as_view(), name='obra_detail'),
    path('obra/add/', ObraCreateView.as_view(), name='obra_create'),
    path('obra/edit/<int:pk>/', ObraUpdateView.as_view(), name='obra_update'),
    path('obra/delete/<int:pk>/', ObraDeleteView.as_view(), name='obra_delete'),
]
