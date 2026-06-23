from django.urls import path
from . import views

# This tells Django that the namespace is 'flight'
app_name = "flight"

urlpatterns = [
    path("", views.index, name="index"), # This path name='index' matches 'flight:index'
    path("<int:flight_id>", views.flight_view, name="flight_view"),
    path("<int:flight_id>/book", views.book, name="book")
]