from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sfood(request):
  return render(request,'sfood.html')

def food3(request):
  return HttpResponse('<center><h1>Most people like homecooked food</h1></center>')