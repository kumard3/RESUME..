from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(home):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def customer(request):
    return render(request, 'customer.html')
