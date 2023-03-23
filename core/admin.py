from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Ads)
class AdsAdmin(TranslationAdmin):
    list_display = ['title', 'text']


@admin.register(Information)
class InformationAdmin(TranslationAdmin):
    list_display = ['text']

@admin.register(Resolve)
class ResolveAdmin(TranslationAdmin):
    list_display = ['title'] 


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    list_display = ['description']


@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ['description']


@admin.register(Agriculture)
class AgricultureAdmin(TranslationAdmin):
    list_display = ['description'] 


@admin.register(Culture)
class CultureAdmin(TranslationAdmin):
    list_display = ['description'] 



@admin.register(News)
class PostAdmin(TranslationAdmin):
    list_display = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'text']
