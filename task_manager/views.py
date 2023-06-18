from django.forms import ValidationError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,  redirect, get_object_or_404
from .models import Task

# Create your views here.



def create_task(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        if Task.objects.filter(title=title).exists():
            return HttpResponse("Title already exists") 
        
        try:
            task = Task.objects.create(user=user,title=title, desc=desc,start_date=start_date,end_date=end_date,priority=priority,status=status)
            task.save()
        
        except ValidationError as e:
            return HttpResponse(str(e))

        # return redirect('task_list')  # Redirect to the task list page after creating the task

    return render(request, 'new_task.html')


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        priority = request.POST.get('priority')
        task.title = title
        task.desc = desc
        task.priority = priority
        task.save()
        return redirect('task_list')
    return render(request, 'task_update.html', {'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/task_list')
    return render(request, 'task_delete.html', {'task': task})

def task_list(request):

    tasks = Task.objects.filter(user= request.user)
    
    return render(request ,'task_list.html', {'tasks':tasks})