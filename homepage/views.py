# homepage/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')  # O caminho correto deve ser 'homepage/home.html'
