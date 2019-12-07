from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import squirrel_site
from .forms import SquirrelForm

def add(request):
    if request.method=="POST":
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/sightings")
    else:
        form=SquirrelForm()
    context={
        'form':form,
            }
    return render(request,'sightings/edit.html',context)

def stats(request):
    total_sites=squirrel_site.objects.count()
    Running_count=squirrel_site.objects.filter(Running=True).count()
    Chasing_count=squirrel_site.objects.filter(Chasing=True).count()
    Climbing_count=squirrel_site.objects.filter(Climbing=True).count()
    Eating_count=squirrel_site.objects.filter(Eating=True).count()
    Foraging_count=squirrel_site.objects.filter(Foraging=True).count()
    Kuks_count=squirrel_site.objects.filter(Kuks=True).count()
    Quaas_count=squirrel_site.objects.filter(Quaas=True).count()
    Moans_count=squirrel_site.objects.filter(Moans=True).count()
    context={
            "Total sites":total_sites,
            "Number of Running squirrels":Running_count,
            "Number of Chasing squirrels":Running_count,
            "Number of Climbing squirrels":Climbing_count,
            "Number of Eating squirrels":Eating_count,
            "Number of Foraging squirrels":Foraging_count,
            "Number of Kuks squirrels":Kuks_count,
            "Number of Quaas squirrels":Quaas_count,
            "Number of Moans squirrels":Moans_count,
    }
    return render(request,"sightings/stats.html",{'context':context})
    

def all_squirrels(request):
    
    squirrels= squirrel_site.objects.all()
    context={
            'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)


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

