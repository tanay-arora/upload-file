from django.contrib import admin
from .models import ticket, summits, events, event_day, feature

@admin.register(ticket)
class ticketAdmin(admin.ModelAdmin):
    list_display = ['id','description','cost']

@admin.register(summits)
class summitsAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug']

@admin.register(events)
class eventsAdmin(admin.ModelAdmin):
    list_display = ['id','title','From','To','summit','slug']

@admin.register(event_day)
class event_dayAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(feature)
class featureAdmin(admin.ModelAdmin):
    list_display = ['id','title']
