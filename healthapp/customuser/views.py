from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'customuser/home.html', {})


def signup(request):
    return render (request, 'customuser/signup.html', {})


def logout(request):
    return render(request, 'customuser/logout.html', {})