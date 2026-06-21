from django.shortcuts import render
from .models import flight
# Create your views here.

def index(request):
    return render(request, "flight/index.html", {
        "flight":flight.objects.all()
    })


def flight_view(request, flight_id):
    f = flight.objects.get(pk=flight_id)
   
    return render(request, "flight/index2.html", {
        "flight": f
    })