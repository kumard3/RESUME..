from django.shortcuts import render
from django.http import HttpResponse

def home(home):
    return render(request, 'index.html')
    #return render(request, 'index.html')