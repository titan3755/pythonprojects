from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import PassWord
from .forms import CreateUser

# Create your views here.
def home(request, *args, **kwargs):
    context = {
        'title': 'Homepage',
    }
    return render(request, 'mainapp/home.html', context)

def about(request, *args, **kwargs):
    context = {}
    return render(request, 'mainapp/about.html', context)

def loginPage(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/passwords')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('/passwords')
            else:
                messages.info(request, 'Username or Password is incorrect!')
        context = {}  
        return render(request, 'mainapp/login.html', context)

def register(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/passwords')
    else:
        form = CreateUser()
        if request.method == 'POST':
                form = CreateUser(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account for ' + user + ' created successfully!')
                    return redirect('/login')
                    
        context = {'form': form, 'title': 'Register'}
        return render(request, 'mainapp/register.html', context)

def logoutUser(request, *args, **kwargs):
    logout(request)
    return redirect('/login')
    
    
@login_required(login_url='/login')
def passwords(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST' and request.POST.get('username-store') != '' and request.POST.get('password-store') != '':
        username = request.POST.get('username-store')
        password = request.POST.get('password-store')
        main = PassWord(username=username, password=password, logged_user=user)
        main.save()
        
    context = {'title': 'Create Usernames and Passwords', 'user': user,}
    return render(request, 'mainapp/passwords.html', context)

@login_required(login_url='/login')
def viewPassword(request, *args, **kwargs):
    context = {'title': 'View'}
    return render(request, 'mainapp/viewpass.html', context)