import os
import sys
import django

# 1. Add the project root directory to the Python path
# This moves up two levels from 'addons.py' to reach 'DjangoSql'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

# 2. Tell Django where your settings file lives 
# (Replace 'YOUR_PROJECT_NAME' with the actual folder name containing your settings.py, e.g., 'DjangoSql')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSql.settings')

# 3. Initialize Django setup
django.setup()

# 4. NOW you can safely import and use your models!
from flight.models import flight

f = flight(
    origin=input("what is your origin: "),
    destination=input("what is your destination: "), 
    duration=int(input("what is your duration :")))
f.save()

print("Flight saved successfully!")