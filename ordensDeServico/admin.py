from django.contrib import admin
from .models import OportunidadesRecente, OrdensServico, Funcionario

admin.site.register(Funcionario)
admin.site.register(OportunidadesRecente)
admin.site.register(OrdensServico)
