from ast import Return
from django.shortcuts import render
from .models import Products

# Create your views here.


def product(request):
    return render(request,'products/product.html',{'pro':Products.objects.all()})

def products(request):
    pro=Products.objects.all()
    x={'pro':pro}

    return render(request,'products/products.html',x)
