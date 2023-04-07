from django.contrib import admin
from .models import *

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['text']

@admin.register(Resolve)
class ResolveAdmin(admin.ModelAdmin):
    list_display = ['title'] 


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['description']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['description']


class AgriCulturePhotoAdmin(admin.StackedInline):
    model = AgriCulturePhoto

@admin.register(Agriculture)
class AgricultureAdmin(admin.ModelAdmin):
    inlines = [AgriCulturePhotoAdmin]
    list_display = ['description']



class CulturePhotoAdmin(admin.StackedInline):
    model = CulturePhoto

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    inlines = [CulturePhotoAdmin]
    list_display = ['description'] 
    


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'text']
