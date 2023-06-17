from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def home(request):

    if request.user.is_anonymous:
         
        return render(request, 'home.html')
    else:
       return redirect('/dashboard/')

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = User.objects.create(password=password, username=username)
        user.set_password(password)
        user.save()
        return redirect('/login/')

    return render(request, 'register.html')


def logoutUser(request):
    logout(request)
    return redirect("/")

def loginUser(request):

    if request.method == "POST":
        username= request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        print(user,username, password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request,'login.html')

        
    return render(request,'login.html')

def dashboard(request):
    if not request.user.is_anonymous:
        return render(request, "dashboard.html")
    else:
        return redirect("/")