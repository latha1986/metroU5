from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def a(request):
    p=Product.objects.all()
    return render(request,'index.html',{"pp":p})