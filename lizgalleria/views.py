from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
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

def image(request,category_name,image_id):
    
    title = 'Image'
    locations = Location.objects.all()
    
    image_category = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html",{'title':title,"image":image, "locations":locations, "image_category":image_category})

