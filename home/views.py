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
        first_name = request.POST.get['first_name']
        last_name = request.POST.get['last_name']
        email = request.POST.get['email']
        username = request.POST.get['username']
        password = request.POST.get['password']
        
        
        user = Register.objects.create(email=email, first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()
        return redirect('/login/')

    return render(request, 'register.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")

def loginUser(request):

    if request.method == "POST":
        email= request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(email=email, password=password)
        print(user,email, password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request,'login.html')

        
    return render(request,'login.html')

def dashboard(request):

    return render(request, "dashboard.html")