from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"index.html")

def singup(request):
    return render(request,"singup.html")