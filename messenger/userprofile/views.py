from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def display_userprofile(request):
    return JsonResponse({'name': 'George',
                        'age': '47',
                        'alma-mater': 'MIPT'})

def contacts(request):
    return JsonResponse({'Vlad0S': '+79965801723',
                        'Ivan': '+79610394717',
                        'Arkadii666': '+6661348483'})
