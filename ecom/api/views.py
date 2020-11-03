from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return JsonResponse({'info': 'Django rest videos', 'name': 'Rahul kumar'})
