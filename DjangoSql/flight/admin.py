from django.contrib import admin
from .models import flight, airport, passenger

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    

admin.site.register(flight, FlightAdmin)
admin.site.register(airport)
admin.site.register(passenger, PassengerAdmin)
