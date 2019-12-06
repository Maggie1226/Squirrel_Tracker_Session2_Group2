from django.shortcuts import render
from django.http import HttpResponse

from .models import squirrel_site
from .forms import SquirrelForm

def all_squirrels(request):
    
    squirrels= squirrel_site.objects.all()
    context={
            'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)

def squirrel_details(request, squirrel_id):
    sq = squirrel_site.objects.get(Unique_Squirrel_ID=squirrel_id)
    return HttpResponse(sq.Name)

def edit_squirrel(request, squirrel_id):
    sq = squirrel_site.objects.get(Unique_Squirrel_ID=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=sq)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'sightings/{squirrel_id}')
    else:
        form = SquirrelForm(instance=sq)

    context = {
        'form': form,
    }

    return render(request, 'sightings/edit.html', context)

