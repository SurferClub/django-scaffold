
from django.urls import path 
from .views import HomeView, CreateProductView 


urlpatterns = [
    path("", HomeView.as_view() , name="homeview"),
    path("addproduct", CreateProductView.as_view() , name="addproduct"),
]