from django.shortcuts import render
from .models import flight
# Create your views here.

def index(request):
    return render(request, "flight/index.html", {
        "flight":flight.objects.all()
        })