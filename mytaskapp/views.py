from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_view(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    context = {'tasks':tasks , 'form':form}
    return render(request, 'mytaskapp/task_view.html', context)

def task_update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    context = {'form':form, 'task':task}
    return render(request, 'mytaskapp/task_update.html', context)

def task_delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('task_view')
    context = {'task':task}
    return render(request, 'mytaskapp/task_delete.html', context)