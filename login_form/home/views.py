from django.shortcuts import render, redirect

def index(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')