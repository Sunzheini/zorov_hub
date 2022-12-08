import random
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from zorov_hub.main_app.models import Groceries, Tasks

# ----------------------------------------------------------------------
# test with a class


class ListDisplay:
    @staticmethod
    def display_list():
        return ['item1', 'item22', 'item3']


# page views
# ----------------------------------------------------------------------

def index(request):
    return render(request, 'index.html')


def games(request):
    return render(request, 'games.html')


def shopping_list(request):
    return render(request, 'shopping_list.html')


def tasks(request):
    return render(request, 'tasks.html')


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

    get_the_groceries_info = get_all_groceries()    # get info from the db-getter
    get_the_tasks_info = get_all_tasks()
    get_1_task = get_a_specific_task()

    context = {
        'process_id': process_id,
        'my_info': [4, 5, 6],
        'value': random.random(),
        'a_dict': {'first_item': 11, 'second_item': '22'},
        'from_class': ListDisplay.display_list(),  # hubavo e da se izpylbnqvat tuk
        'datetime': datetime.now(),

        'groceries_list': get_the_groceries_info,
        'tasks_list': get_the_tasks_info,
        'task_1': get_1_task,
    }
    return render(request, 'process_description.html', context)


# ----------------------------------------------------------------------
# not used
def return_to_home(request):
    return redirect('index')


# get data from db
# ----------------------------------------------------------------------
"""
Groceries.objects.all()             # get all objects (__str__) // Select
Groceries.objects.create()          # create a new object // Insert

# s filter bazata ni vryshta samo iskanite neshta i e po-leko za memory!!!
Groceries.objects.filter(age=36)    # filter // Select + Where
Groceries.objects.update()          # update // Update
Groceries.objects.raw('SELECT * ')  # directly sql

Groceries.objects.all().delete()    # iztriva vsichko
"""


def get_all_groceries():
    # Bez list e `Query Set`, ne se izpylnqva na momenta
    all_groceries = Groceries.objects.all() \
        .order_by('id', 'grocery_name')     # moje da se chain-va (i pak e 1 zaqvka)
    return all_groceries


def get_all_tasks():
    all_tasks = list(Tasks.objects.all())
    return all_tasks


def get_a_specific_task():
    # get returns an object, not a query set
    specific_task = Tasks.objects.get(pk=1)
    return specific_task


# not used
def delete_grocery(request, pk):
    to_delete = get_object_or_404(Groceries, pk=pk)
    to_delete.delete()
    return redirect('index')
