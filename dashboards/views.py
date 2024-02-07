from django.shortcuts import get_list_or_404, get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from members.forms import UpdatePasswdForm, UpdateProfileForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User
from pages.models import Notification, Package,Flight
from django.contrib import messages
import sweetify





def is_regular_user(user):
    return not user.is_staff 
def is_admin(user):
    return user.is_staff  


# Create your views here.
@user_passes_test(is_admin)
def dashboard(request):
    users = User.objects.all()
    notifications = Notification.objects.all()
    return render(request,'dashboard.html',{'users':users,'notifications':notifications})

@login_required
def profil(request):
    return render(request,'profile.html')

@user_passes_test(is_regular_user)
def checkout(request):
    packages = Package.objects.filter(checked_out_by=request.user)
    flights = Flight.objects.filter(checked_out_by=request.user)
    return render(request,'checkout.html',{'packages':packages,'flights':flights})

@login_required
def users(request):
    users = User.objects.all()
    return render(request,'Users.html',{'users':users})

@login_required
def delete_user(request,usk):
    user = get_object_or_404(User, username=usk)
    if user.delete() :
        notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            type= "USER",
            message = f"{request.user} DELETED user {user.first_name} {user.last_name}",  # Customize the message based on the action
        )
        notification.save()
        messages.success(request, ' USER DELETED !!')
        return redirect('/Users')  
    
@login_required
def update_user(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            type= "USER",
            message = f"{request.user.first_name} has updated his profile",  
        )
            notification.save()
            messages.success(request, 'CHANGES SAVED !!')
            return redirect('/profil')  
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})

def update_pwd(request):
    if request.method == 'POST':
        form = UpdatePasswdForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            type= "USER",
            message = f"{request.user.first_name} has updated his password",  
        )
            notification.save()
            update_session_auth_hash(request, user)  # Imptnt!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/profil')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UpdatePasswdForm(request.user)
    return render(request, 'changepwd.html', {
        'form': form
    })

@login_required
def add_flight(request):
    if request.method == 'POST':
            new_flight = Flight(
                depart=request.POST['depart'],
                ps1=request.POST['ps1'],
                ps2=request.POST['ps2'],
                hour_d=request.POST['hour_d'],
                destination=request.POST['destination'],
                hour_a=request.POST['hour_a'],
                price=request.POST['price'],
                classe =request.POST['class'],
            )
            new_flight.save()
            notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            type= "FLIGHT",
            message = f"{request.user} Has added new flight from {new_flight.depart} ----> to {new_flight.destination}",  # Customize the message based on the action
            )
            notification.save()
            messages.success(request,'FLIGHT ADDED SUCCESSFULLY !!')
            return redirect('/add_flight')
    return render(request, 'add_flight.html')


@login_required
def add_pack(request):
    if request.method == 'POST':
            uploaded_image = request.FILES.get('image')
            new_Pack = Package(
                country=request.POST['country'],
                discription=request.POST['description'],
                date=request.POST['period'],
                price=request.POST['price'],
                personce=request.POST['nb'],
                pack_image = uploaded_image,
            )
            new_Pack.save()
            notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            image = new_Pack.pack_image,
            type= "PACKAGE",
            message = f"{request.user} ADDED new package - {new_Pack.country} ",  
            )
            notification.save()
            messages.success(request,'PACKAGE ADDED SUCCESSFULLY !!')
            return redirect('/add_pack')
    return render(request, 'add_package.html')

@login_required
def delete_pack_from_check(request,id):
    pack = get_object_or_404(Package, id=id)
    pack.checked_out_by.remove(request.user)
    notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            image = pack.pack_image,
            type= "PACKAGE",
            message = f"{request.user.first_name} DELETED {pack.country}'s PACKAGE from his checkout",  # Customize the message based on the action
        )
    notification.save()
    messages.success(request, 'You have been removed that package.')
    return redirect('/checkout')

@login_required
def delete_flight_from_check(request,id):
    flight = Flight.objects.get(id=id)
    flight.checked_out_by.remove(request.user)
    notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            type= "FLIGHT",
            message = f"{request.user.first_name} DELETED flight from {flight.depart} ----> to {flight.destination} from his checkout",  # Customize the message based on the action
        )
    notification.save()
    messages.success(request, 'You have been removed that flight.')
    return redirect('/checkout')



# @user_passes_test(is_regular_user)
def paiment(request):
    user = request.user
    if request.method == 'POST':
        packages_to_update = Package.objects.filter(checked_out_by=user)
        for package in packages_to_update:
            package.checked_out_by.remove(user)
        flights_to_update = Flight.objects.filter(checked_out_by=user)
        for flight in flights_to_update:
            flight.checked_out_by.remove(user)   
        notification = Notification(
            recipient=request.user,
            last_name = request.user.last_name,
            type= "DOLLAR",
            message = f"{request.user.first_name} PAID & VALIDATED  his checkout",  # Customize the message based on the action
        )
        notification.save()
        messages.success(request, 'CHECKOUT VALIDATED !!')
        return redirect('/checkout')
    return render(request,"paiment.html")

def delete_notif(request,id):
        notif = Notification.objects.get(id=id)
        notif.delete()
        return redirect('/dashboard')
