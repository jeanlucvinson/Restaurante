from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def reserva(request):
    return render(request, 'tela_reserva.html')


@csrf_exempt
def salvar_reserva(request):
    color = request.POST.get('color')
    quantity = request.POST.get('quantity')
    print('oi')