from django.contrib import admin
from .models import *



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'text']
