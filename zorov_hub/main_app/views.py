import random
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('page: index')


def games(request):
    return HttpResponse('page: games')


def shopping_list(request):
    return HttpResponse('page: shopping list')


# mikro-kontrolerite vkyshti naglasi
def control_of_home(request):
    return HttpResponse('page: control of home')


# avotmatizaciq bylgarene  / solarni paneli
def control_of_garden(request):
    return HttpResponse('page: control of garden')


def chat(request):
    return HttpResponse('page: chat')


def process_description(request, process_id):
    context = {
        'process_id': process_id,
        'my_info': [4, 5, 6],
        'value': random.random(),
        'a_dict': {'first_item': 11, 'second_item': '22'},
    }
    return render(request, 'process_description.html', context)
