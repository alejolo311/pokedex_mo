from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon
from django.forms.models import model_to_dict

def json(request, name):

    format = request.GET["format"] if 'format' in request.GET else None
    if format == "json":
        try:
            pk = Pokemon.objects.get(name=name)
        except Pokemon.DoesNotExist:
            return JsonResponse({"error": "pokemon not found"}, status=404)
        return JsonResponse(model_to_dict(pk))
    else:
        data = {}
        try:
            pk = Pokemon.objects.get(name=name)
            data['pokemon'] = pk
            if pk.prevolution:
                data['pre'] = Pokemon.objects.get(id=pk.prevolution)
            if pk.evolution:
                data['ev'] = []
                for i in pk.evolution:
                    data['ev'].append(Pokemon.objects.get(id=i))
            return render(request, 'individual.html', context=data)
        except Pokemon.DoesNotExist:
            return HttpResponse("<h1> pokemon not found </h1>", status=404)


def all(request):

    format = request.GET["format"] if 'format' in request.GET else None
    if format == "json":
        try:
            pk = Pokemon.objects.all().order_by('id')

        except Pokemon.DoesNotExist:
            return JsonResponse({"error": "pokemon not found"}, status=404)
        pkms = []
        for pokemon in pk:
            pkms.append(model_to_dict(pokemon))

        return JsonResponse(pkms, safe=False)
    else:
        data = {}
        try:
            pk = Pokemon.objects.all().order_by('id')
            data['pokemon'] = pk
            return render(request, 'all.html', context=data)
        except Pokemon.DoesNotExist:
            return HttpResponse("<h1> pokemon not found </h1>", status=404)


def ev_chain(request, id):

    format = request.GET["format"] if 'format' in request.GET else None
    if format == "json":
        try:
            pk = Pokemon.objects.filter(evolution=id)
        except Pokemon.DoesNotExist:
            return JsonResponse({"error": "pokemon not found"}, status=404)
        pkms = []
        for pokemon in pk:
            pkms.append(model_to_dict(pokemon))

        return JsonResponse(pkms, safe=False)
    else:
        data = {}
        try:
            pk = Pokemon.objects.filter(chain=id)
            data["ev"] = True
            data['pokemon'] = pk
            return render(request, 'all.html', context=data)
        except Pokemon.DoesNotExist:
            return HttpResponse("<h1> pokemon not found </h1>", status=404)
