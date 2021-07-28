import os
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request, *args, **kwargs):
    context = {'title': 'PhotoBytes Home'}
    return render(request, 'mainapp/home.html', context)

def signup(request, *args, **kwargs):
    context = {'title': 'Sign Up'}
    return render(request, 'mainapp/signup.html', context)

def login(request, *args, **kwargs):
    context = {'title': 'Login'}
    return render(request, 'mainapp/login.html', context)

def pricing(request, *args, **kwargs):
    context = {'title': 'Pricing'}
    return render(request, 'mainapp/pricing.html', context)

def about(request, *args, **kwargs):
    context = {'title': 'About'}
    return render(request, 'mainapp/about.html', context)

def privacy(request, *args, **kwargs):
    context = {'title': 'Privacy Policy'}
    return render(request, 'mainapp/privacy.html', context)