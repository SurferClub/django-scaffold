from django.db import models

# Create your models here.

class Comprador(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Caja(models.Model):
    name = models.CharField(max_length=15,default="")
    valorEntrada = models.IntegerField(default=0)
    montos = models.IntegerField(default=0)
    saldo = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Cajero(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Entrada(models.Model):
    caja = models.ForeignKey(Caja,on_delete=models.CASCADE)
    monto = models.IntegerField()
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    date_joined = models.DateField()
