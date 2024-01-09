from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home_page(request):
    count = User.objects.count()
    return render(request, 'hompage/index.html' ,{'count':count})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Welcome'  +  user, 'Please login' )
            return redirect('home-page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

