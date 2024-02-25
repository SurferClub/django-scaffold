from django.shortcuts import render
from django.views.generic import TemplateView , CreateView
from .forms import ProductForm
from django.urls import reverse_lazy

from .models import  Product
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ProductForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['productlist'] = Product.objects.all()
        return context

class CreateProductView(CreateView): 
    template_name = "add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('homeview')

class ProductDetailView(TemplateView): 
    template_name= 'productdetails.html'

