from django.urls import path
from . import views
urlpatterns = [
    path('birthday_view', views.birthday_view, name='birthday'), # This maps the root URL to the birthday_view in views.py
] 