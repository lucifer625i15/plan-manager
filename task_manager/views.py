from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render,  redirect, get_object_or_404
from .models import Task

# Create your views here.

def home(request):

    return render(request, 'index.html')

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        priority = request.POST['priority']
        status = request.POST['status']

        if Task.objects.filter(title=title).exists():
            return HttpResponse("title already exists") 
        
        try:
            task = Task.objects.create(title=title,desc=desc,start_date=start_date,end_date=end_date,priority=priority,status=status)
            task.save()
        
        except ValidationError as e:
            return HttpResponse(str(e))

        # return redirect('task_list')  # Redirect to the task list page after creating the task

    return render(request, 'add.html')


def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        title = request.POST.get['title']
        desc = request.POST.get['description']
        priority = request.POST.get['priority']
        task.title = title
        task.desc = desc
        task.priority = priority
        task.save()
        return redirect('task_list')
    return render(request, 'task_update.html', {'task': task})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})