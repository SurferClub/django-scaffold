from django.shortcuts import render,get_object_or_404
from .models import generador
# Create your views here.
import random

def generate(request):
       
    chart = 'abcdefhgijklmnopqrstuvxyz'
    num = "1234567890"
    specialChart = '-[{<>}]'
    lista = chart + num + specialChart
    password = ''
    for x in range(10):
        randomChart = random.choice(lista)
        password += randomChart
    
    data = generador.objects.create(password = password)
    data.save() 

    return render(request, 'generador/password.html',{"password": password})

def home(request):
    passwords = generador.objects.all()
    return render(request, 'generador/home.html',{'passwords': passwords})
