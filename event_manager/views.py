from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def create_event(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        location = request.POST.get('location')


        if Event.objects.filter(title=title).exists():
            return HttpResponse("Title already exists") 
        
        try:
            event = Event.objects.create(user=user,title=title, desc=desc,date=date, location=location)
            event.save()
        
        except ValidationError as e:
            return HttpResponse(str(e))

        # return redirect('task_list')  # Redirect to the task list page after creating the task

    return render(request, 'new_event.html')

def event_update(request, event_id):

    event = Event.objects.get(id=event_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        date = request.POST.get('date')
        
        event.title = title
        event.description = description
        event.location = location
        event.date = date
        event.save()
        
        return redirect('/')
    
    return render(request, 'edit_event.html', {'event': event})

def event_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'delete_event.html', {'event': event})
