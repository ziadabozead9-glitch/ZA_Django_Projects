from django.shortcuts import render, get_object_or_404
from .models import flight, passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "flight/index.html", {
        "flights": flight.objects.all()
    })



def flight_view(request, flight_id):
    f = get_object_or_404(flight, pk=flight_id)
    return render(request, "flight/index2.html", {
        "flight": f,                              
        "passengers": f.passengers.all(),
        "non_passengers": passenger.objects.exclude(flights=f).all(),                
    })



def book(request, flight_id):
    if request.method == "POST":
        current_flight = get_object_or_404(flight, pk=flight_id)
        passenger_id = int(request.POST.get("passenger"))
        current_passenger = passenger.objects.get(pk=passenger_id)
        current_passenger.flights.add(current_flight)
        return HttpResponseRedirect(reverse("flight:flight_view", args=(current_flight.id,)))
    


