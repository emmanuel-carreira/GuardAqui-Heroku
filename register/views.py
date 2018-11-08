from django.shortcuts import render

# Create your views here.

#Homepage
def home(request):
    return render(request, 'register/home.html')

#Login page
def login(request):
    return render(request, 'register/login.html')