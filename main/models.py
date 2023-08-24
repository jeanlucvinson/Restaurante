from django.db import models

# Create your models here.
class usuario(models.Model):
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
 
class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_cliente

class Data(models.Model):
    data_hora = models.DateTimeField()

    def __str__(self):
        return self.data_hora.strftime("%d-%m-Y% %H:%M")
        # return self.data_hora.strftime("%Y-%m-%d %H:%M")
    
class NumeroPessoas(models.Model):
    numero_pessoas = models.IntegerField

class Reserva(models.Model):
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.ForeignKey(Data, on_delete=models.CASCADE)
    numero_pessoas = models.ForeignKey(NumeroPessoas, on_delete=models.CASCADE)

