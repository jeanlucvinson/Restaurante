from django.urls import path

from . import views

urlpatterns = [
    path('', views.tela_principal, name='tela_principal'),
    path('', views.reserva, name='tela_reserva'),
]