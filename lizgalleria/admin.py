from django.contrib import admin

from lizgalleria.models import Category, Location,Image

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)
