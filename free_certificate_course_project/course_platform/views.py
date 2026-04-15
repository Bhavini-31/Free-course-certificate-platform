from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Platform


# Create your views here.

def home(request):
    platforms = Platform.objects.all()
    return render(request, 'home.html', {'platforms': platforms})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

