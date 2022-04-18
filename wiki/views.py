from django.shortcuts import render, redirect
from .forms import RegistrerForm
from django.contrib.auth import login

def home(request):
    return render(request, 'wiki/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrerForm
    
    return render(request, 'registration/register.html', {"form": form})