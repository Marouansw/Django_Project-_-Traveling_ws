from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from members import forms
# Create your views here.


def home(request):
  return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def service(request):
    return render(request,'service.html')

def destination(request):
    return render(request,'destination.html')


def package(request):
    return render(request,'package.html')


def contact(request):
   return render(request,'contact.html')


def register(request):
    return render(request,'ragister.html')
