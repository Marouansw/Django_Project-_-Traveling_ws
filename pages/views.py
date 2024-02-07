from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.template import RequestContext, loader
from .models import Package,Flight,Notification
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import sweetify



from members import forms
# Create your views here.


def home(request):
  package = Package.objects.all()
  depart_list = Flight.objects.values_list('depart', flat=True).distinct()
  destination_list = Flight.objects.values_list('destination', flat=True).distinct()
  return render(request,'index.html',{'package':package,'depart_list':depart_list,'destination_list':destination_list})



def about(request):
    depart_list = Flight.objects.values_list('depart', flat=True).distinct()
    destination_list = Flight.objects.values_list('destination', flat=True).distinct()
    return render(request,'about.html',{'depart_list':depart_list,'destination_list':destination_list})


def service(request):
    depart_list = Flight.objects.values_list('depart', flat=True).distinct()
    destination_list = Flight.objects.values_list('destination', flat=True).distinct()
    return render(request,'service.html',{'depart_list':depart_list,'destination_list':destination_list})

def destination(request):
    depart_list = Flight.objects.values_list('depart', flat=True).distinct()
    destination_list = Flight.objects.values_list('destination', flat=True).distinct()
    return render(request,'destination.html',{'depart_list':depart_list,'destination_list':destination_list})

@login_required
def package(request):
    package = Package.objects.all()
    depart_list = Flight.objects.values_list('depart', flat=True).distinct()
    destination_list = Flight.objects.values_list('destination', flat=True).distinct()
    return render(request,'package.html',{'package':package,'depart_list':depart_list,'destination_list':destination_list})

@login_required
def checkout_package(request,cntr):
    pack = get_object_or_404(Package, country=cntr)
    if request.user in pack.checked_out_by.all():
        sweetify.info(request, 'PACKAGE IS ALREADY ADDED TO CARD!!', button='Ok', timer=3000)
    else:
        pack.checked_out_by.add(request.user)
        pack.save()  
        notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            image = pack.pack_image,
            type= "PACKAGE",
            message = f"{request.user.first_name} Checked out {pack.country}'s PACKAGE ",  # Customize the message based on the action
        )
        notification.save()
        sweetify.success(request,'PACKAGE ADDED TO CARD!!',button='Ok', timer=3000)

    return redirect('/package.html')  

@login_required
def delete_package(request,id):
    pack = Package.objects.get(id=id)
    notification = Notification(
            recipient=request.user,
            image = pack.pack_image,
            type= "PACKAGE",
            message = f"{request.user} DELETED {pack.country}'s PACKAGE ",  # Customize the message based on the action
        )
    notification.save()
    pack.delete() 
    sweetify.success(request, ' PACKAGE DELETED !!')
    return redirect('/package.html')  


@login_required
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
            return redirect('/index.html')
    else:
            return redirect('/index.html')
    
@login_required
def checkout_flight(request,fid):  
    flight = get_object_or_404(Flight,id=fid)
    if request.user in flight.checked_out_by.all():
        sweetify.info(request, 'FLIGHT IS ALREADY ADDED TO CARD!!', button='Ok', timer=3000)
    else:
        flight.checked_out_by.add(request.user)
        flight.save()
        notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            type= "FLIGHT",
            message = f"{request.user.first_name} Checked out the flight from {flight.depart} ----> to {flight.destination}",  # Customize the message based on the action
        )
        notification.save()
        sweetify.success(request,'FLIGHT ADDED TO CARD!!',button='Ok', timer=3000)

    return redirect('/index.html')  # Redirect to the user's profile page or another appropriate page
    

@login_required
def delete_flight(request,id):
    flight = Flight.objects.get(id=id)
    notification = Notification(
            recipient=request.user,
            type= "FLIGHT",
            message = f"{request.user} DELETED the flight from {flight.depart} ----> to {flight.destination}",  # Customize the message based on the action
        )
    notification.save()
    flight.delete() 
    sweetify.success(request, ' FLIGHT DELETED !!')
    return redirect('/index.html')  


def contact(request):
    depart_list = Flight.objects.values_list('depart', flat=True).distinct()
    destination_list = Flight.objects.values_list('destination', flat=True).distinct()
    return render(request,'contact.html',{'depart_list':depart_list,'destination_list':destination_list})



