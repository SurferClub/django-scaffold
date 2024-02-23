
from django.urls import path 
from .views import HomeView, CreateProductView , cajero, detailView


urlpatterns = [
    path("", HomeView.as_view() , name="homeview"),
    path("addproduct", CreateProductView.as_view() , name="addproduct"),
    path("caja", cajero , name='caja' ),
    path("details", detailView, name="detail")
]