from django.contrib import admin
from .models import *

@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = ['id']

