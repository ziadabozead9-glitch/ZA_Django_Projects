from django.urls import path
from . import views

app_name = "gmail"
urlpatterns = [
    path('index', views.index, name='index'), # This is the only path in the app
]