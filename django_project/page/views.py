from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myhome(request):
    return HttpResponse("welcome")

def home(request):
    return render(request, ('home_page.html'))

def about(request):
    return render(request,('about_page.html'))









