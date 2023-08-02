from django.shortcuts import render, redirect
from .forms import VoluntarioForm
from .models import Voluntario

def formulario_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = VoluntarioForm()
    
    return render(request, 'formulario_voluntario.html', {'form': form})

def agradecimiento(request):
    return render(request, 'agradecimiento.html')

def voluntarios_totales(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'voluntarios_totales.html', {'voluntarios': voluntarios})

