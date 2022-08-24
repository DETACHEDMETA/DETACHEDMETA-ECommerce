from itertools import product
from django.shortcuts import render
from .models import category_model , product_model

# Create your views here.


def home_view(request) :

    category = category_model.objects.all()
    product = product_model.objects.all()
    top = product.filter(top_product=True)
    
    context = {
        'category' : category ,
        'top_product' : top[::-1] ,
    }
    return render(request, 'home/home.html',context)


def detail_view(request,pk) :
    product = product_model.objects.all()
    product_info = product.filter(id=pk)
    context = {
        'product' : product_info ,
    }
    return render(request, 'home/detail_product.html',context)


def product_page_view(request) :
    product = product_model.objects.all()

    context = {
        'product' : product[::-1] ,
    }
    return render(request, 'home/product_page.html',context)

