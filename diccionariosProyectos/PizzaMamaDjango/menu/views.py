from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from .models import Plat


# Create your views here.
def pizzas(request):
    plats = Plat.objects.filter(categorie='PI')
    return render(request, 'menu/pizzas.html', {'plats': plats})


def pates(request):
    plats = Plat.objects.filter(categorie='PA')
    return render(request, 'menu/pates.html', {'plats': plats})


def salades(request):
    plats = Plat.objects.filter(categorie='SA')
    return render(request, 'menu/salades.html', {'plats': plats})


def desserts(request):
    plats = Plat.objects.filter(categorie='DE')
    return render(request, 'menu/desserts.html', {'plats': plats})


def api_get_plats(request):
    plats = Plat.objects.all().order_by('prix')
    json = serializers.serialize("json", plats)
    return HttpResponse(json)
