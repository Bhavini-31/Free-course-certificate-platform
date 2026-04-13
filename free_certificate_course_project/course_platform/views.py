from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Platform
from .forms import RegisterForm, LoginForm

# 🔐 Home (Protected)
@login_required(login_url='/login/')
def home(request):
    platforms = Platform.objects.all()
    return render(request, 'home.html', {'platforms': platforms})

# 📄 Existing Pages (UNCHANGED)
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


# 🆕 Signup
def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    return render(request, 'register.html', {'form': form})


# 🔐 Login
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user:
                login(request, user)
                return redirect('/')

    return render(request, 'login.html', {'form': form})


# 🚪 Logout
def logout_view(request):
    logout(request)
    return redirect('/login/')