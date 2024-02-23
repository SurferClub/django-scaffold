from django.db import models

# Create your models here.

class Product(models.Model):
    title =models.CharField(max_length=80)
    banner = models.ImageField(upload_to='product/banner')

    def __str__(self):
        return self.title
    

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    images = models.ImageField(upload_to='product/images')



class Caja(models.Model):
    name = models.CharField(max_length=15,default="")
    valorEntrada = models.IntegerField(default=0)
    montos = models.IntegerField(default=0)
    saldo = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    
class Comprador(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class Entrada(models.Model):
    caja = models.ForeignKey(Caja,on_delete=models.CASCADE)
    monto = models.IntegerField()

    

 