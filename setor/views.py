from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required, permission_required

from . import models
from . import forms

@login_required
@never_cache
@permission_required('setor.view_setor', raise_exception=True)
def index(request):
    try:
        setores = models.Setor.objects.all().order_by('nome')
    except models.Setor.DoesNotExist:
        return HttpResponse("Nenhum departamento encontrado")
    context = {"setores": setores, "title": "Departamentos"}
    template = "setor/index.html"
    
    return render(request, template, context)

@login_required
@permission_required('setor.add_setor', raise_exception=True)
def create(request):
    if request.method == 'POST':    
        form = forms.SetorForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('setor:index')
        else:
            return HttpResponse("Erro ao criar departamento")
        
    else:
        form = forms.SetorForm()
            
    template = 'setor/create.html'
    context = { 
        'msg' : 'Adicionar departamento',
        'form': form,
    }
    
    return render(request, template, context)

@login_required
@permission_required('setor.change_setor', raise_exception=True)
def update(request, id_setor):
    try:
        setor = models.Setor.objects.get(id=id_setor)
    except models.Setor.DoesNotExist:
        return HttpResponse("Departamento não encontrado")

    if request.method == 'POST':
        form = forms.SetorForm(request.POST, instance=setor)
        
        if form.is_valid():
            form.save()
            return redirect('setor:index')
        else:
            return HttpResponse("Informações inválidas")
    else:
        form = forms.SetorForm(instance=setor)
        
    template = 'setor/update.html'
    context = {
        'msg' : 'Editar departamento',
        'form': form,
    }
    
    return render(request, template, context)

@login_required
@permission_required('setor.delete_setor', raise_exception=True)
def delete(request, id_setor):
    try:
        models.Setor.objects.get(id=id_setor).delete()
    except models.Setor.DoesNotExist:
        return HttpResponse("Departamento não encontrado")
    
    return redirect("setor:index")

@login_required
@never_cache
@permission_required('setor.view_setor', raise_exception=True)
def details(request, id_setor):
    try:
        setor = models.Setor.objects.get(id=id_setor)
    except models.Setor.DoesNotExist:
        return HttpResponse("Departamento não encontrado")
    
    context = {'setor': setor}
    template = 'setor/details.html'
    
    return render(request, template, context)
