from django.shortcuts import render
from ..sightings.models import squirrel_site

def squirrel_map(request):
    return render(request,'map/default.html',{})


