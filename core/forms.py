from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import *

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

'''
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'fecha_atencion', 'anamesis', 'medicamentos_recetados', 'examenes_indicados', 'diagnostico']
        widgets = {
            'fecha_atencion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'anamesis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'medicamentos_recetados': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'examenes_indicados': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }'''

class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
        fields = ['rut','nombre','apellido','fecha_nacimiento','genero','telefono','correo']

