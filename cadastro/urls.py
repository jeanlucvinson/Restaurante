from django.urls import path

from . import views

urlpatterns = [
    path('', views.tela_cadastro, name='tela_cadastro'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    # path('', views.reserva, name='tela_reserva'),
]