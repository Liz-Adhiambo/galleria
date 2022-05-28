from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Sunsplash'

    return render(request, 'gallery.html', {'title':title, 'images':images, 'locations':locations})

