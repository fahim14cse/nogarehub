from cgitb import text
from multiprocessing import Value
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView,
)

from myapp.models import Contract

# Create your views here.

def deshboard(request):
    return render(request,'home.html')
def home(request):
    return render(request,'home.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

class ShowData(ListView):
    
    def get(self, request, *args, **kwargs):      


        context = {
            'data': Contract.objects.all()
   
        }
        return render(request, 'show_data.html', context)

def contract(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        print("this is post")
        values = Contract(name=name, email=email, desc=desc)
        values.save()
    return render(request,'contract.html')

