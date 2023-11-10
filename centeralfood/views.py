from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cfood(request):
  return render(request,'cfood.html')

def food2(request):
  return HttpResponse('<center><h1>Most people like thali</h1></center>')