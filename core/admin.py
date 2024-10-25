from django.contrib import admin
from . models import *
# Register your models here.

class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'especialidad']
    search_fields = ['nombre', 'apellido', 'especialidad']
    list_per_page = 10
    list_filter = ['especialidad']

admin.site.register(TipoMedico)
admin.site.register(Medico, MedicoAdmin)
