from django.db import models

# Create your models here.

class TipoMedico(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.ForeignKey(TipoMedico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Paciente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    rut = models.CharField(max_length = 12, blank=False)
    nombre = models.CharField(max_length = 40, blank=False)
    apellido = models.CharField(max_length = 40, blank=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=False)
    telefono = models.CharField(max_length = 12, blank=False) 
    correo = models.EmailField(blank=False)

fields = ['rut','nombre','apellido','fecha_nacimiento','genero','telefono','correo']


import logging

class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('django.request')

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code >= 400:
            self.logger.error(f'Error {response.status_code} en la URL {request.path}')
        return response