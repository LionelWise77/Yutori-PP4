from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_spa(request):
    return HttpResponse("Welcome to Yutori Spa!")