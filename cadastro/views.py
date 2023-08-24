from django.shortcuts import render

# Create your views here.
def tela_cadastro(request):
    return render(request, 'tela_cadastro.html')

def cadastrar(request):

    user = request.get('usuario')
    senha = request.get('senha')