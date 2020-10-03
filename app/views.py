from django.shortcuts import render, HttpResponse
from django.views import View



def home(request):
    return HttpResponse("This is homepage.")