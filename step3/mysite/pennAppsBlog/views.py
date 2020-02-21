from django.shortcuts import render

def index(request):
    return render(request, 'home.html')
# Create your views here.

def Page1(request):
    return render(request, 'page1.html')

def Page2(request):
    return render(request, 'page2.html')
