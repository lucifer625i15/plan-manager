from django.forms import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,  redirect, get_object_or_404
from .models import Travel

# Create your views here.



def create_travel(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        if travel.objects.filter(title=title).exists():
            return HttpResponse("Title already exists") 
        
        try:
            travel = travel.objects.create(user=user,title=title, desc=desc,start_date=start_date,end_date=end_date,priority=priority,status=status)
            travel.save()
        
        except ValidationError as e:
            return HttpResponse(str(e))

        # return redirect('travel_list')  # Redirect to the travel list page after creating the travel

    return render(request, 'new_travel.html')


def travel_update(request):
    travel = get_object_or_404(Travel)
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        priority = request.POST.get('priority')
        travel.title = title
        travel.desc = desc
        travel.priority = priority
        travel.save()
        return redirect('travel_list')
    return render(request, 'travel_update.html', {'travel': travel})

def travel_delete(request, travel_id):
    travel = get_object_or_404(travel, id=travel_id)
    if request.method == 'POST':
        travel.delete()
        return redirect('/travel_list')
    return render(request, 'travel_delete.html', {'travel': travel})

def travel_list(request):

    travels = travel.objects.filter(user= request.user)
    
    return render(request ,'travel_list.html', {'travels':travels})