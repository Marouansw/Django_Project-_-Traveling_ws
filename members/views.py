from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader,redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from members.forms import RegisterUserForm
# Create your views here.

def register_user(request):
    if request.user.is_authenticated:
        messages.success(request,"Already Logged in!! Logout First ")
        return redirect('/index.html')
    if request.method == "POST" :
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user1 = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"REGISTRED SUCCESSFULLY !! ")
            return redirect('/index.html')
    else:
        form = RegisterUserForm()
        

    return render(request,'authenticate/register.html',{'form':form,'user': request.user})


def login_user(request):
    if request.user.is_authenticated:
        messages.success(request,"Already Logged in!! Logout First ")
        return redirect('/index.html')

    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            print("User authenticated:", user.username)
            messages.success(request,"Login Succeed !! ")
            print(request.user)
            return redirect('/index.html')
        else:
            messages.success(request,"Username or password incorrect !! ")
            return redirect('/login.html')
            
    else:
        return render(request,'authenticate/login.html')
    



def logout_view(request):
    logout(request)
    messages.success(request,"You are logged out !!")
    return HttpResponseRedirect('/index.html')

