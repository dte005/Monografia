from django.urls import path
from .views import principal, listaOrdens, criarOrdem, listarecurso
from .views import osdetalhes, topicoajuda, emconstrucao, exportar

urlpatterns = [
    path('home/', principal, name='principal'),
    path('home/listaordens/', listaOrdens, name='lista_ordens' ),
    path('home/listarecurso/<int:id>', listarecurso, name='lista_recurso'),
    path('home/criar/<int:id>/', criarOrdem, name='criar_ordem'),
    path('home/ajuda/', topicoajuda, name = 'topico_ajuda'),
    path('home/emconstrucao/', emconstrucao, name= 'em_construcao'),
    path('home/exportar/', exportar, name='exportar'),
    path('home/osdetalhes/<int:id>/', osdetalhes, name = 'os_detalhes'),
]
