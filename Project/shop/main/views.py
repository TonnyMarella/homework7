from django.shortcuts import render
from .models import Product
from django.views import View
from .forms import UserOurRegistration

def index(request):
    return render(request, 'main/index.html')


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()
        print(request.session.session_key)
    return render(request, 'main/product.html', context)


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'main/shop.html', context)
