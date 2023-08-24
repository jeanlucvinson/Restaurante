from django.urls import path

from . import views

urlpatterns = [
    path('', views.tela_cadastro, name='tela_cadastro'),
    path('', views.cadastrar, name='cadastrar'),
    # path('', views.reserva, name='tela_reserva'),
]