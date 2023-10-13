# i created this

from django.http import HttpResponse
from django.shortcuts import render
from .models import Unit, UpgradeLevel1, UnitUpgrade1, Weapon

def index(request):
    units = Unit.objects.all()
    params = {'unit':units}
    print(params)
    return render(request, 'index.html', params)


def getunit_details(unit_id):
    unit = Unit.objects.get(id=unit_id)
    primary_weapon = Weapon.objects.get(name=unit.primary_weapon)
    if unit.secondary_weapon:
        secondary_weapon = Weapon.objects.get(name=unit.secondary_weapon)
    else:
        secondary_weapon = None
    all_list = []
    for i in unit.upgrades.all():
        upgrade = UnitUpgrade1.objects.get(name=i)
        x = upgrade.levels.all()
        all_levels=[]
        for j in x:
            about_level = [j.level, j.benefit, j.requirement,j.cost, j.time]
            all_levels.append(about_level)
        all_list.append([i, all_levels])
    
    params = {'unit' : unit, 'primary_weapon': primary_weapon, 'secondary_weapon':secondary_weapon, 'upgrades': all_list}

    return params

def unit1(request):
    return render(request, 'about.html', getunit_details(1))

def unit2(request):
    return render(request, 'about.html', getunit_details(2))


def unit3(request):
    units = Unit.objects.all()
    params = {'unit' : units[3]}
    return render(request, 'about.html', params)

def unit4(request):
    units = Unit.objects.all()
    params = {'unit' : units[4]}
    return render(request, 'about.html', params)

def unit5(request):
    units = Unit.objects.all()
    params = {'unit' : units[5]}
    return render(request, 'about.html', params)

def unit6(request):
    units = Unit.objects.all()
    params = {'unit' : units[6]}
    return render(request, 'about.html', params)

def unit7(request):
    units = Unit.objects.all()
    params = {'unit' : units[7]}
    return render(request, 'about.html', params)

def unit8(request):
    units = Unit.objects.all()
    params = {'unit' : units[8]}
    return render(request, 'about.html', params)

def unit9(request):
    units = Unit.objects.all()
    params = {'unit' : units[9]}
    return render(request, 'about.html', params)

def unit10(request):
    units = Unit.objects.all()
    params = {'unit' : units[10]}
    return render(request, 'about.html', params)

def unit11(request):
    units = Unit.objects.all()
    params = {'unit' : units[11]}
    return render(request, 'about.html', params)