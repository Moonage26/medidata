from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from . import views 

urlpatterns = [
    path('', index, name="index"), # PAGINA DE INICIO
    path('index/', index, name="index"),
    path('admin/', admin, name="admin"),
    path('medico/', medico, name="medico"),
    path('paciente/', paciente, name="paciente"),
    path('quienessomos/' , quienessomos, name="quienessomos"),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('registrar_paciente/', registrar_paciente, name='registrar_paciente'),
    path('nueva_consulta/', nueva_consulta, name='nueva_consulta'),
    path('listar_pacientes/', listar_pacientes, name='listar_pacientes'),
    path('get-data/', views.get_supabase_data, name='get_supabase_data'),
]
