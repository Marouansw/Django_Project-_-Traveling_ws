from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Package

from members import forms
# Create your views here.


def home(request):
  package = Package.objects.all()
  return render(request,'index.html',{'package':package})



def about(request):
    return render(request,'about.html')


def service(request):
    return render(request,'service.html')

def destination(request):
    return render(request,'destination.html')


def package(request):
    package = Package.objects.all()
    return render(request,'package.html',{'package':package})


def contact(request):
   return render(request,'contact.html')


def register(request):
    return render(request,'ragister.html')
