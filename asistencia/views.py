from django.shortcuts import render, redirect, get_object_or_404
from .models import Asistencia
from .forms import AsistenciaForm


def listar(request):
    registros = Asistencia.objects.all().order_by('-fecha')
    return render(request, 'lista.html', {'registros': registros})


def crear(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = AsistenciaForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nuevo registro'})


def editar(request, id):
    registro = get_object_or_404(Asistencia, id=id)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = AsistenciaForm(instance=registro)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar registro'})


def eliminar(request, id):
    registro = get_object_or_404(Asistencia, id=id)
    if request.method == 'POST':
        registro.delete()
    return redirect('listar')