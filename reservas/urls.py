from django.urls import path

from . import views

urlpatterns = [
    path('', views.reserva, name='reserva'),
    path('salvar_reserva', views.salvar_reserva, name='salvar_reserva'),
]