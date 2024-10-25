# admin.py

from django.contrib import admin
from .models import Obra, TipoTrabalho

class TipoTrabalhoAdmin(admin.ModelAdmin):
    list_display = ['nome']

class ObraAdmin(admin.ModelAdmin):
    list_display = ['numero_identificativo', 'cliente', 'estado']

admin.site.register(TipoTrabalho, TipoTrabalhoAdmin)
admin.site.register(Obra, ObraAdmin)
