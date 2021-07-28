from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    context = {}
    return render(request, 'mainapp/home.html', context)