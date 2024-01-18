from django.shortcuts import get_list_or_404, get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from members.forms import UpdatePasswdForm, UpdateProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User
from pages.models import Package,Flight
from django.contrib import messages
import sweetify



# Create your views here.
@login_required
def dashboard(request):
    return render(request,'dashboard.html')
@login_required
def profil(request):
    return render(request,'profile.html')

@login_required
def checkout(request):
    packages = get_list_or_404(Package,checked_out='yes')
    for p in packages:
        print(p.type)
        print(p.price)
        print(p.country)
    return render(request,'checkout.html',{'packages':packages})

@login_required
def users(request):
    users = User.objects.all()
    return render(request,'Users.html',{'users':users})

@login_required
def delete_user(request,usk):
    user = get_object_or_404(User, username=usk)
    if user.delete() :
        messages.success(request, ' USER DELETED !!')
        return redirect('/Users')  # Redirect to the user's profile page or another appropriate page

@login_required
def update_user(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'CHANGES SAVED !!')
            return redirect('/profil')  # Redirect to the user's profile page or another appropriate page
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})

def update_pwd(request):
    if request.method == 'POST':
        form = UpdatePasswdForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/profil')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UpdatePasswdForm(request.user)
    return render(request, 'changepwd.html', {
        'form': form
    })


   