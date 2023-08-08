from django.http import HttpResponse
from django.shortcuts import redirect, render


def tela_principal(request):
    return render(request, 'tela_principal.html')

# def reserva(request):
#     return render(request, 'tela_reserva.html')