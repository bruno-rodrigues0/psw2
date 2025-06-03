from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required,  permission_required
from django.contrib.auth.models import Group

from . import models, forms

from datetime import datetime

@login_required
@never_cache
@permission_required('pessoa.view_pessoa', raise_exception=True)
def index(request):
    try:
        pessoas = models.Pessoa.objects.all().order_by('nome')
    except models.Pessoa.DoesNotExist:
        return HttpResponse("Nenhuma pessoa encontrada")
    context = {"pessoas": pessoas, "title": "Bem Vindo!"}
    template = "pessoa/index.html"
    
    return render(request, template, context)

@login_required
@permission_required('pessoa.add_pessoa', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = forms.PessoaCreationForm(request.POST)
        
        if form.is_valid():
            pessoa = form.save(commit=False)
            default_group = Group.objects.get(name="default")
            setores = form.cleaned_data.get('setores')
            if setores:
                pessoa.add_em = datetime.now()
            pessoa.save()
            form.save_m2m()
            pessoa.groups.add(default_group)
            return redirect('pessoa:index')
        else:
            return HttpResponse("Erro ao criar pessoa")
        
    else:
        form = forms.PessoaCreationForm()
            
    template = 'pessoa/create.html'
    context = { 
        'msg' : 'Adicionar pessoa',
        'form': form,
    }
    
    return render(request, template, context)

@login_required
@permission_required('pessoa.change_pessoa', raise_exception=True)
def update(request, id_pessoa):
    try:
        pessoa = models.Pessoa.objects.get(id=id_pessoa)
    except models.Pessoa.DoesNotExist:
        return HttpResponse("Pessoa não encontrada")

    if request.method == 'POST':
        form = forms.PessoaChangeForm(request.POST, instance=pessoa)
        
        if form.is_valid():
            pessoa = form.save(commit=False)
            setores = form.cleaned_data.get('setores')
            if setores:
                pessoa.add_em = datetime.now().date() 
            pessoa.save()
            form.save_m2m()
            return redirect('pessoa:index')
        else:
            context = {
                'msg': 'Editar pessoa',
                'form': form,
                'errors': form.errors
            }
            return render(request, 'pessoa/update.html', context)
    else:
        form = forms.PessoaChangeForm(instance=pessoa)
        
    template = 'pessoa/update.html'
    context = {
        'msg' : 'Editar pessoa',
        'form': form,
    }
    
    return render(request, template, context)

@login_required
@permission_required('pessoa.delete_pessoa', raise_exception=True)
def delete(request, id_pessoa):
    try:
        models.Pessoa.objects.get(id=id_pessoa).delete()
    except models.Pessoa.DoesNotExist:
        return HttpResponse("Pessoa não encontrada")
    
    return redirect("pessoa:index")

@login_required
@never_cache
@permission_required('pessoa.view_pessoa', raise_exception=True)
def details(request, id_pessoa):
    try:
        pessoa = models.Pessoa.objects.get(id=id_pessoa)
    except models.Pessoa.DoesNotExist:
        return HttpResponse("Pessoa não encontrada")
    
    context = {'pessoa': pessoa}
    template = 'pessoa/details.html'
    
    return render(request, template, context)
