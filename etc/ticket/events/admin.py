from django.contrib import admin
from .models import Venue, Event

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('id','name','address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title','venue','starts_at','on_sale','capacity')
    list_filter = ('on_sale','venue')
    search_fields = ('title',)
