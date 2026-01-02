from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario
from .forms import FuncionarioForm

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/listar.html', {'funcionarios': funcionarios})

def adicionar_funcionario(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_funcionarios')
    return render(request, 'funcionarios/form.html', {'form': form})

def atualizar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('listar_funcionarios')
    return render(request, 'funcionarios/form.html', {'form': form})

def deletar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    return redirect('listar_funcionarios')
