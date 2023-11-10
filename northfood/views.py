from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def nfood(request):
  return render(request,'nfood.html')

def food1(request):
  return HttpResponse('<center><h1>Most people like streetfood</h1></center>')

