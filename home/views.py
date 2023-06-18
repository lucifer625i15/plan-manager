from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from expense_tracker.models import Expense
from travel_manager.models import *
from task_manager.models import Task
from event_manager.models import Event
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def home(request):
    if request.user.is_anonymous:
         
        return render(request, 'home.html')
    else:
       return redirect('/dashboard/')

def register(request):

    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = User.objects.create(password=password, name=name, username=username)
        user.set_password(password)
        user.save()
        return redirect('/login/')

    return render(request, 'register.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")

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

    users = request.user
    expenses = Expense.objects.all()
    events = Event.objects.all()
    tasks = Task.objects.all()
    # travels = Travel.objects.all()
    return render(request, "dashboard.html", {'expenses':expenses, 'events': events, 'tasks':tasks})
        