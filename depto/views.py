from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required, permission_required

from . import models
from . import forms

@login_required
@never_cache
@permission_required('depto.view_depto', raise_exception=True)
def index(request):
    try:
        deptos = models.Depto.objects.all().order_by('nome')
    except models.Depto.DoesNotExist:
        return HttpResponse("Nenhum departamento encontrado")
    context = {"deptos": deptos, "title": "Departamentos"}
    template = "depto/index.html"
    
    return render(request, template, context)

@login_required
@permission_required('depto.add_depto', raise_exception=True)
def create(request):
    if request.method == 'POST':    
        form = forms.DeptoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('depto:index')
        else:
            return HttpResponse("Erro ao criar departamento")
        
    else:
        form = forms.DeptoForm()
            
    template = 'depto/create.html'
    context = { 
        'msg' : 'Adicionar departamento',
        'form': form,
    }
    
    return render(request, template, context)

@login_required
@permission_required('depto.change_depto', raise_exception=True)
def update(request, id_depto):
    try:
        depto = models.Depto.objects.get(id=id_depto)
    except models.Depto.DoesNotExist:
        return HttpResponse("Departamento não encontrado")

    if request.method == 'POST':
        form = forms.DeptoForm(request.POST, instance=depto)
        
        if form.is_valid():
            form.save()
            return redirect('depto:index')
        else:
            return HttpResponse("Informações inválidas")
    else:
        form = forms.DeptoForm(instance=depto)
        
    template = 'depto/update.html'
    context = {
        'msg' : 'Editar departamento',
        'form': form,
    }
    
    return render(request, template, context)

@login_required
@permission_required('depto.delete_depto', raise_exception=True)
def delete(request, id_depto):
    try:
        models.Depto.objects.get(id=id_depto).delete()
    except models.Depto.DoesNotExist:
        return HttpResponse("Departamento não encontrado")
    
    return redirect("depto:index")

@login_required
@never_cache
@permission_required('depto.view_depto', raise_exception=True)
def details(request, id_depto):
    try:
        depto = models.Depto.objects.get(id=id_depto)
    except models.Depto.DoesNotExist:
        return HttpResponse("Departamento não encontrado")
    
    context = {'depto': depto}
    template = 'depto/details.html'
    
    return render(request, template, context)
