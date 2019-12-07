from django.shortcuts import render
import sys,os,inspect
import random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from sightings.models import squirrel_site
def squirrel_map(request):
    squirrels = squirrel_site.objects.all()
    sightings = squirrels[:40]
    context={
            'sightings':sightings
            ,}
    return render(request,'map/default.html',context)


