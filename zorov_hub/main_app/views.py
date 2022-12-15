import random
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from zorov_hub.main_app.forms import NameForm, GameForm
from zorov_hub.main_app.models import Groceries, Tasks, Games

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

    if request.method == 'GET':
        form = GameForm()  # ako e get syzdava formata prazna
    else:  # request.method == 'post'
        form = GameForm(request.POST, request.FILES)
        form.is_valid()  # proverka sprqmo zadadenoto v formata

    # ne sym go probval vmesto ostanaloto za zapazvane
    # -----------------
    #     if form.is_valid():
    #         form.save()

    # write to db - second option
    # ---------------------------------------------------------------------
        Games.objects.create(
            **form.cleaned_data
        )
        make_them_slugs()

    # ---------------------------------------------------------------------
    context = {
        'game_form': form,
    }

    return render(request, 'games.html', context)


def shopping_list(request):

    # form
    # ---------------------------------------------------------------------
    a_grocery_name = None
    a_grocery_count = None
    if request.method == 'GET':
        form = NameForm()       # ako e get syzdava formata prazna
    else:   # request.method == 'post'
        form = NameForm(request.POST)
        form.is_valid()         # proverka sprqmo zadadenoto v formata
        a_grocery_name = form.cleaned_data['form_grocery_name']
        a_grocery_count = form.cleaned_data['form_grocery_count']

    # write to db
    # ---------------------------------------------------------------------
        Groceries.objects.create(
            grocery_name=a_grocery_name,
            grocery_count=a_grocery_count
        )

    # ---------------------------------------------------------------------
    context = {
        'name_form': form,
        'a_grocery_name': a_grocery_name,
        'a_grocery_count': a_grocery_count,
    }
    return render(request, 'shopping_list.html', context)


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

    make_them_slugs()

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

        'games': Games.objects.all(),
    }
    return render(request, 'process_description.html', context)


def game_details(request, pk, slug):
    context = {
        'current_game': get_object_or_404(Games, pk=pk, slug=slug)
    }
    return render(request, 'game_details.html', context)


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


# ----------------------------------------------------------------------
def make_them_slugs():
    all_games = Games.objects.all()
    for g in all_games:
        g.slug = slugify(g.game_name)
    Games.objects.bulk_update(all_games, ['slug'])

# ----------------------------------------------------------------------


# not used
def delete_grocery(request, pk):
    to_delete = get_object_or_404(Groceries, pk=pk)
    to_delete.delete()
    return redirect('index')


# # --------------------------------------------------------------------------
# # profile / no profile different homepage
#
#
# def get_profile():
#     try:
#         return Profile.objects.get()
#     except Profile.DoesNotExist as ex:
#         return None
#
#
# def add_profile(request):
#     if get_profile() is not None:
#         return redirect('index')
#
#     if request.method == 'GET':
#         form = ProfileForm()
#     else:
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'core/home-no-profile.html', context)
#
#
# def index(request):
#     profile = get_profile()
#     if profile is None:
#         return redirect('add profile')
#
#     context = {
#         'albums': Album.objects.all(),
#     }
#
#     return render(request, 'core/home-with-profile.html', context)
#
#
# # --------------------------------------------------------------------------

