import random
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect


# ----------------------------------------------------------------------
class ListDisplay:
    @staticmethod
    def display_list():
        return ['item1', 'item22', 'item3']

# ----------------------------------------------------------------------


def index(request):
    return render(request, 'index.html')


def games(request):
    return render(request, 'games.html')


def shopping_list(request):
    return render(request, 'shopping_list.html')


# mikro-kontrolerite vkyshti naglasi
def control_of_home(request):
    return render(request, 'control_of_home.html')


# avotmatizaciq bylgarene  / solarni paneli
def control_of_garden(request):
    return render(request, 'control_of_garden.html')


def chat(request):
    return render(request, 'chat.html')


# ----------------------------------------------------------------------
def process_description(request, process_id):
    context = {
        'process_id': process_id,
        'my_info': [4, 5, 6],
        'value': random.random(),
        'a_dict': {'first_item': 11, 'second_item': '22'},
        'from_class': ListDisplay.display_list(),  # hubavo e da se izpylbnqvat tuk
        'datetime': datetime.now(),
    }
    return render(request, 'process_description.html', context)


# ----------------------------------------------------------------------
def return_to_home(request):
    return redirect('index')



