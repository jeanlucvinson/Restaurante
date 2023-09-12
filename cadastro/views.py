from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def tela_cadastro(request):
    print('oi')
    return render(request, 'tela_cadastro.html')

@csrf_exempt
def cadastrar(request):

    user = request.get('usuario')
    senha = request.get('senha')