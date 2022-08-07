from ast import Return
from django.shortcuts import render
from .models import Products

# Create your views here.


def product(request):
    return render(request,'products/product.html',{'pro':Products.objects.all()})

def products(request):
    return render(request,'products/products.html',{'pro':Products.objects.all()})