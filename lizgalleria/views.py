from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, 'landing.html')

# Create your views here.
