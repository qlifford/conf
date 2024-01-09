from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UserForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Welcome'  +  user, 'Please login here' )
            return redirect('login_page')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_view')
        else:
            messages.info(request,'Ivalid Credentials')
            return redirect('login_page')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return render(request, 'mytaskapp/task_view.html')

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