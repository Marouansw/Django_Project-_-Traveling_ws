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


def package(request):
    package = Package.objects.all()
    return render(request,'package.html',{'package':package})

def flight(request):
    if request.method == 'POST':
        depart_location = request.POST.get('depart')
        destination = request.POST.get('destination')
        depart_d = request.POST.get('depart_date')
        return_d = request.POST.get('return_date')
        # Retrieve the list of flights based on the given criteria
        if depart_location and destination and depart_d and return_d:
            flights = Flight.objects.filter(depart=depart_location, destination=destination)

        # Render the result template with the flights and dates
            if not flights:
                return render(request, 'Flight_result.html', {
                'depart_d': depart_d,
                'return_d': return_d,
                'no_flights': True,
            })
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
    if flight.checked_out=='no':
        flight.checked_out = 'yes'
        flight.save()
        sweetify.success(request,'FLIGHT ADDED TO CARD!!',button='Ok', timer=3000)
    else:
        sweetify.info(request, 'FLIGHT IS ALREADY ADDED TO CARD!!', button='Ok', timer=3000)

    return redirect('/index.html')  # Redirect to the user's profile page or another appropriate page
    


def checkout_package(request,cntr):
    pack = get_object_or_404(Package, country=cntr)
    if pack.checked_out=='no':
        pack.checked_out = 'yes'
        pack.save()
        sweetify.success(request,'PACKAGE ADDED TO CARD!!',button='Ok', timer=3000)
    else:
        sweetify.info(request, 'PACKAGE IS ALREADY ADDED TO CARD!!', button='Ok', timer=3000)

    return redirect('/index.html')  # Redirect to the user's profile page or another appropriate page
    


def contact(request):
   return render(request,'contact.html')


def register(request):
    return render(request,'ragister.html')
