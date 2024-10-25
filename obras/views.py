from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Obra
from .forms import ObraForm

class ObraListView(ListView):
    model = Obra
    template_name = 'obras/obra_list.html'
    context_object_name = 'obras'

class ObraDetailView(DetailView):
    model = Obra
    template_name = 'obras/obra_detail.html'
    context_object_name = 'obra'

class ObraCreateView(CreateView):
    model = Obra
    form_class = ObraForm
    template_name = 'obras/obra_form.html'
    success_url = reverse_lazy('obra_list')

    def form_valid(self, form):
        # Não é necessário chamar form.save_m2m() aqui
        return super().form_valid(form)

class ObraUpdateView(UpdateView):
    model = Obra
    form_class = ObraForm
    template_name = 'obras/obra_form.html'
    success_url = reverse_lazy('obra_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save_m2m()  # Salva os campos ManyToMany após o commit do objeto
        return response

class ObraDeleteView(DeleteView):
    model = Obra
    template_name = 'obras/obra_confirm_delete.html'
    success_url = reverse_lazy('obra_list')
