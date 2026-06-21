from django.urls import path
from . import views  

urlpatterns = [
    path("index", views.index, name="index"), # Changed from views.flight to views.index
    path("<int:flight_id>", views.flight_view, name="flight"), # Changed from views.flight to views.flight_view
]