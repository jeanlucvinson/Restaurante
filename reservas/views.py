from django.shortcuts import render

# Create your views here.


def reserva(request):
    return render(request, 'tela_reserva.html')