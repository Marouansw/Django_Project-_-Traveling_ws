from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def service(request):
  template = loader.get_template('service.html')
  return HttpResponse(template.render())

def destination(request):
  template = loader.get_template('destination.html')
  return HttpResponse(template.render())

def package(request):
  template = loader.get_template('package.html')
  return HttpResponse(template.render())