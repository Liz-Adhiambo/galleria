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
    location = request.GET.get('location')

    if location ==None:
         images = Image.objects.all()
    else:
        
        images= Image.objects.filter(image_location__name=location)

   
    

    return render(request, 'gallery.html', {'images':images, 'locations':locations})

def image(request,category_name,image_id):
    
    title = 'Image'
    locations = Location.objects.all()
    
    image_category = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html",{'title':title,"image":image, "locations":locations, "image_category":image_category})

def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{"message": message})

def location_filter(request, image_location):
    locations = Location.objects.all()
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    
    return render(request, 'location.html', { 'images':images, 'locations':locations, 'location':location})


