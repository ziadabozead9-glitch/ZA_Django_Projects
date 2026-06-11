from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.
def birthday_view(request):
    now = datetime.datetime.now()
    
    return render(request, 'mybirthday/mybirthday.html', {
        'name': 'miro'.capitalize(),
        'mybirthday': now.month == 6 and now.day == 8

    })