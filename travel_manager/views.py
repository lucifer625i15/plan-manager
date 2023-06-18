from django.shortcuts import render,  redirect, get_object_or_404


# Create your views here.

def travel_list(request):

    # travels = travel.objects.filter(user= request.user)
    
    return render(request ,'home.html')