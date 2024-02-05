from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.template import RequestContext, loader
from .models import Package,Flight
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import sweetify



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

@login_required
def package(request):
    package = Package.objects.all()
    return render(request,'package.html',{'package':package})

@login_required
def checkout_package(request,cntr):
    pack = get_object_or_404(Package, country=cntr)
    if request.user in pack.checked_out_by.all():
        sweetify.info(request, 'PACKAGE IS ALREADY ADDED TO CARD!!', button='Ok', timer=3000)
    else:
        pack.checked_out_by.add(request.user)
        pack.save()
        sweetify.success(request,'PACKAGE ADDED TO CARD!!',button='Ok', timer=3000)

    return redirect('/index.html')  

@login_required
def delete_package(request,id):
    pack = Package.objects.filter(id=id)
    if pack.delete() :
        sweetify.success(request, ' PACKAGE DELETED !!')
        return redirect('/package.html')  



def flight(request):
    if request.method == 'POST':
        depart_location = request.POST.get('depart')
        destination = request.POST.get('destination')
        depart_d = request.POST.get('depart_date')
        return_d = request.POST.get('return_date')
        if depart_location and destination and depart_d and return_d:
            flights = Flight.objects.filter(depart=depart_location, destination=destination)
            return render(request, 'Flight_result.html', {
               'flights': flights,
               'depart_d': depart_d,
               'return_d': return_d,
        })
        else:
            messages.success(request, ' Invalid form submission!')
            return render(request, 'index.html')
    else:
            return render(request, 'index.html')
    
@login_required
def checkout_flight(request,fid):  
    flight = get_object_or_404(Flight,id=fid)
    if request.user in flight.checked_out_by.all():
        sweetify.info(request, 'FLIGHT IS ALREADY ADDED TO CARD!!', button='Ok', timer=3000)
    else:
        flight.checked_out_by.add(request.user)
        flight.save()
        sweetify.success(request,'FLIGHT ADDED TO CARD!!',button='Ok', timer=3000)

    return redirect('/index.html')  # Redirect to the user's profile page or another appropriate page
    

@login_required
def delete_flight(request,id):
    flight = Flight.objects.filter(id=id)
    if flight.delete() :
        sweetify.success(request, ' FLIGHT DELETED !!')
        return redirect('/index.html')  


def contact(request):
   return render(request,'contact.html')


def register(request):
    return render(request,'ragister.html')
