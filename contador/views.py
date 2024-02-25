from django.shortcuts import render , HttpResponseRedirect , get_object_or_404
from .models import Caja
from django.urls import reverse

# Create your views here.

def cajero(request):
    valorEntrada = Caja.objects.all()
    return render(request, "caja.html",{'valorEntrada':valorEntrada})

def detailView(request):
    valorEntrada = get_object_or_404(Caja)
    try:
        valores = valorEntrada.valorEntrada.get(request.POST["valor"])
    except (KeyError, Caja.DoesNotExist):
        return render(request, "caja.html", {
            "valores" : valores, 
            "error_message": "no hay valores"
        })
    else: 
        valores.save()

        return HttpResponseRedirect(reverse("caja"))