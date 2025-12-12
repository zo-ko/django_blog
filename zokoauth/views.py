from django.shortcuts import render

# Create your views here.

def user_rigister(request):
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')
