from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from .forms import * 
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def base(request):
    return render(request, 'core/base.html')

def admin(request):
    return render(request, 'core/admin.html')

@login_required
def medico(request):
    return render(request, 'core/medico.html', {'nombre_usuario': request.user.get_full_name() or request.user.username})

@login_required
def paciente(request):
    return render(request, 'core/paciente.html', {'nombre_usuario': request.user.get_full_name() or request.user.username})

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='Administradores').exists(): #si el usuario está en el grupo administradores
                    return redirect('admin')  # Redirige a la URL del administrador
                elif user.groups.filter(name='Medicos').exists():
                    return redirect('medico')  # Redirige a la URL del médico
                elif user.groups.filter(name='Pacientes').exists():
                    return redirect('paciente')  # Redirige a la URL del paciente
    else:
        form = CustomAuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def admin(request):
    return render(request, 'core/admin.html')

def registrar_paciente(request):
    datos = {
        'form' : PacienteForm()
    }

    if request.method == 'POST':
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            datos['msj'] = "Paciente guardado correctamente"

    return render(request, 'core/paciente/registrar_paciente.html', datos)

def listar_pacientes(request):
    listaPacientes = Paciente.objects.all()

    datos = {
        'lista' : listaPacientes
    }

    return render(request, 'core/paciente/listar_pacientes.html',datos)

def nueva_consulta(request):
    return render(request, 'core/nueva_consulta.html')