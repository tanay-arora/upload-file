from django.contrib import admin
from .models import current_speakers, past_speakers

@admin.register(current_speakers)
class cspeakersAdmin(admin.ModelAdmin):
    list_display = ['id','name','company','designation']

@admin.register(past_speakers)
class pspeakersAdmin(admin.ModelAdmin):
    list_display = ['id','name','company','designation']
