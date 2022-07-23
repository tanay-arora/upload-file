from django.contrib import admin
from .models import sponsors_category, sponsors, investors

@admin.register(sponsors_category)
class sponsors_categoryAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(sponsors)
class sponsorsAdmin(admin.ModelAdmin):
    list_display = ['id','title','url']

@admin.register(investors)
class investorsAdmin(admin.ModelAdmin):
    list_display = ['id','name','company','designation']
