from django.urls import path

from . import views

urlpatterns = [
    path('tela/', views.tela_principal, name='tela_principal'),
]