from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect,get_object_or_404
from .forms import SightForm
from django.db.models import Avg, Max, Min, Count
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request,'sightings/homepage.html')

def map(request):
    sights = Sight.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'sightings/map.html',context)

def sighting(request):
    squirrel = Sight.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift','Age']
    context = {
            'squirrels': squirrel,
            'fields':fields
        }
    return render(request, 'sightings/list.html',context)

def add_squirrel(request):
    if request.method == "POST":
        form= SightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightForm()
    context ={
            'form':form,
        }
    return render(request,'sightings/add.html',context)

def update(request,Unique_Squirrel_Id):
    squirrel = Sight.objects.filter(Unique_Squirrel_Id=Unique_Squirrel_Id).first()
    if request.method == 'POST':
        form = SightForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightForm(instance = squirrel)

    context = {
            'form':form,
            }
    return render(request, 'sightings/update.html', context)

def get_stats(request):
    am_shift = 0
    pm_shift = 0
    adult = 0
    juvenile = 0
    running = 0
    climbing = 0
    eating = 0
    foraging = 0
    kuks = 0
    quaas = 0
    moans = 0
    tail_flags = 0
    tail_switches = 0

    for squirrel in Sight.objects.all():
        if squirrel.Shift == 'AM':
            am_shift += 1
        if squirrel.Shift == 'PM':
            pm_shift += 1
        if squirrel.Age == 'Adult':
            adult += 1
        if squirrel.Age == 'Juvenile':
            juvenile += 1
        if squirrel.Running == True:
            running +=1
        if squirrel.Climbing== True:
            climbing +=1
        if squirrel.Eating == True:
            eating += 1
        if squirrel.Foraging == True:
            foraging += 1
        if squirrel.Kuks == True:
            kuks += 1
        if squirrel.Quaas == True:
            quaas += 1
        if squirrel.Moans == True:
            moans += 1
        if squirrel.Tail_Flags == True:
            tail_flags += 1
        if squirrel.Tail_Twitches == True:
            tail_switches += 1

    context = {
        'adult': adult,
        'juvenile': juvenile,
        'AM_shift': AM_shift,
        'PM_shift': PM_shift,
        'running': running,
        'climbing': climbing,
        'eating': eating,
        'foraging': foraging,
        'kuks': kuks,
        'quaas': quaas,
        'moans': moans,
        'tail_flags': tail_flags,
        'tail_twitches': tail_twitches,
        }
    return render(request, 'sightings/stats.html', context)
