from itertools import product
from django.shortcuts import render , redirect
from .models import category_model , product_model
import razorpay
from django.views.decorators.csrf import csrf_exempt


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



@csrf_exempt
def detail_view(request,pk) :
    product = product_model.objects.all()
    product_info = product.filter(id=pk)
    price = product_info.values("price") 
    print(price[0])
    #  payment with Razorpay
    if request.method == 'POST' :
        client = razorpay.Client(auth=("rzp_test_MAGS2JFcBu5vr1", "ZWueXiUCqEgLzdgln0Q7OqgM"))

        DATA = {
            "amount": 1000 ,
            "currency": "INR",
            "receipt": "receipt#1",
            "notes": {
                "key1": "value3",
                "key2": "value2"
            }
        }
        payment = client.order.create(data=DATA)

        context = {
        'product' : product_info ,
        'payment' : payment,
            }
        print("**********************************")
        print("**********************************")
        print(payment , payment['id'])
        print("**********************************")
        print("**********************************")
        # return render(request, 'home/detail_product.html',context)
        return redirect("/download_confirm/"+payment['id']+"/"+pk)

    #  payment with Razorpay
    else :
        print("**********************************")
        print("**********************************")
        # print(payment)
        print("**********************************")
        print("**********************************")
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


@csrf_exempt
def download_confirm_view(request,order,pk) :
    product = product_model.objects.all()
    product_download = product.filter(id=pk)


    context = {
        'product' : product_download ,
    }
    return render(request, 'home/download_confirm.html',context)

