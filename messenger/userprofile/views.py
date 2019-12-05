from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def display_userprofile(request):
    if request.method == 'GET':
        return JsonResponse({'name': 'George',
                            'age': '47',
                            'alma-mater': 'MIPT'})
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def contacts(request):
    if request.method == 'GET':
        return JsonResponse({'Vlad0S': '+79965801723',
                            'Ivan': '+79610394717',
                            'Arkadii666': '+6661348483'})
    else:
        return HttpResponseNotAllowed(['GET'])
