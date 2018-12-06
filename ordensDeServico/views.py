from django.shortcuts import render, redirect, get_object_or_404
from .models import OportunidadesRecente, Funcionario, OrdensServico
import random
from datetime import date


#serviços gerais
def servicosGerais():
    oportunidades = OportunidadesRecente.objects.all()
    ordens = OrdensServico.objects.all()
    recursos = Funcionario.objects.filter(func_status=False)
    m=0
    for z in oportunidades:
        m = m + 1
    n=0
    for y in ordens:
        n = n + 1
    p=0
    for f in recursos:
        p = p + 1
    lista=[m,n,p]
    return lista

def principal(request):

    #filtro de datas
    oportunidades_rec = OportunidadesRecente.objects.filter(op_data=date.today())
    oportunidades_ant = OportunidadesRecente.objects.exclude(op_data=date.today())

    lista = servicosGerais()
    return render(
    request,
    'index.html',
    {'lista_atual':oportunidades_rec,
     'lista_antiga':oportunidades_ant,
     'total_op': lista[0],
     'total_ord':lista[1],
     'total_rec':lista[2]})

def listaOrdens(request):
    ordens = OrdensServico.objects.all()
    lista = servicosGerais()
    return render(
    request,
    'listaordens.html',
    {'total_op': lista[0],
    'total_ord':lista[1],
    'lista':ordens,
    'total_rec':lista[2]})

def criarOrdem(request, id):
    ordens = OrdensServico.objects.all()
    ident = get_object_or_404(OportunidadesRecente, pk=id)
    nome = ident.op_nome
    descricao = ident.op_descricao

    ordem = OrdensServico.objects.create(os_nome=nome, os_recursos=0, os_descricao=descricao)
    ordem.save()

    lista = servicosGerais()
    return render(
    request,
    'listaordens.html',
    {'lista':ordens,
    'total_op': lista[0],
    'total_ord':lista[1],
    'total_rec':lista[2]})

def listarecurso(request, id):
    recurso = Funcionario.objects.filter(func_status=False)

    #verificar como será realizado a seleção de funcionarios
    #ident = get_object_or_404(OrdensServico, pk=id)
    #nome = ident.os_nomes
    #recurso = ident.os_recurso
    #descricao = ident.os_descricao

    #recurso = recurso + 1

    #estado = OrdensServico.objects.update(os_nome = nome, os_recurso = recurso, os_descricao=descricao)

    lista = servicosGerais()
    return render(request, 'listarecurso.html', {
    'recursos':recurso,
    'total_op': lista[0],
    'total_ord': lista[1],
    'total_rec':lista[2],
    'estado': int(id)})

def topicoajuda(request):
    lista = servicosGerais()
    return render(request,
    'ajuda.html',
    {'total_op':lista[0],
    'total_ord': lista[1],
    'total_rec': lista[2]})

def osdetalhes(request, id):
    ident = get_object_or_404(OrdensServico, pk=id)
    lista = servicosGerais()
    #entrar com formulário
    return render(request,
    'osdetalhes.html',
    {'detalhes':ident,
    'total_op': lista[0],
    'total_ord': lista[1],
    'total_rec': lista[2]})

def emconstrucao(request):
    lista = servicosGerais()
    return render(request, 'emconstrucao.html',
    {'total_op':lista[0],
    'total_ord':lista[1],
    'total_rec':lista(2)})

def exportar(request):
    lista = servicosGerais()
    return render(request, 'export.html',
    {'total_op':lista[0],
    'total_ord':lista[1],
    'total_rec':lista[2]})
