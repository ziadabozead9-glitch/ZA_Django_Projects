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
    # 1. Using get_object_or_404 prevents the app from crashing if an invalid ID is requested
    f = get_object_or_404(flight, pk=flight_id)
   
    return render(request, "flight/index2.html", {
        "flight": f,                              
        "passengers": f.passengers.all(),
        # FIXED: Pass 'f' (the specific flight object instance) instead of the 'flight' model class
        "non_passengers": passenger.objects.exclude(flights=f).all(),                
    })

def book(request, flight_id):
    if request.method == "POST":
        # 1. Get the current flight instance
        current_flight = get_object_or_404(flight, pk=flight_id)
        
        # 2. FIXED: Changed passenger.object.get to passenger.objects.get (added 's')
        #    and properly extracted the value from request.POST
        passenger_id = int(request.POST.get("passenger"))
        current_passenger = passenger.objects.get(pk=passenger_id)
        
        # 3. FIXED: Changed passenger.flight.add to current_passenger.flights.add 
        #    to match the related ManyToMany field name ('flights') in your model
        current_passenger.flights.add(current_flight)
        
        # 4. FIXED: Added 'flight:' namespace to match your app configuration,
        #    and properly structured args as a tuple (flight_id,)
        return HttpResponseRedirect(reverse("flight:flight_view", args=(current_flight.id,)))