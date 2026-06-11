from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):  # Changed 'returns' to 'request'
    now = datetime.datetime.now()
    return render(request, 'app1/app1.html', {
        'mybirthday': now.month == 6 and now.day == 26,
        'name': 'Ziad'.capitalize(),
    })