from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Platform

# 👇 ADD THIS
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    platforms = Platform.objects.all()
    return render(request, 'home.html', {'platforms': platforms})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# 👇 ADD THIS NEW VIEW
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   # goes to login page
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})