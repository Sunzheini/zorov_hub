import random
from datetime import datetime

from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from zorov_hub.main_app.forms import NameForm, GameForm, ProfileForm, ProfileEditForm, ProfileDeleteForm
from zorov_hub.main_app.models import Groceries, Tasks, Games, Profile


# --------------------------------------------------------------------------
# test with a class

class ListDisplay:
    @staticmethod
    def display_list():
        return ['item1', 'item22', 'item3']


# class-based views
# --------------------------------------------------------------------------

class ControlView:
    @classmethod
    def get_view1(cls):
        return ControlView().control_of_garden

    # mikro-kontrolerite vkyshti naglasi
    def control_of_garden(self, request):
        return render(request, 'control_of_garden.html')


# class ControlView2(views.View):
#     def get(self, request):     # prenapisvame gotoviq metod get
#         return self.control_of_home(request)
#
#     # avotmatizaciq bylgarene  / solarni paneli
#     def control_of_home(self, request):
#
#         context = {
#             'some_text': 'some text...'
#         }
#
#         return render(request, 'control_of_home.html', context)


class ControlView2(views.TemplateView):
    template_name = 'control_of_home.html'
    extra_context = {'some_text': 'some text...'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Games.objects.all()
        return context


# Index function based view
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# profile / no profile different homepage

def get_profile():
    try:
        return Profile.objects.get(pk=5)        # ToDo: Authentication (now looks for a profile with pk=5)
    except Profile.DoesNotExist as ex:
        return None


def add_profile(request):
    # if get_profile() is not None:
    #     return redirect('index')      # was used in the exam prep to avoid bypassing

    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'add_profile.html', context)


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'profiles': Profile.objects.all(),
    }

    return render(request, 'index.html', context)
#
#
# def details_profile(request, pk):
#     pass


# --------------------------------------------------------------------------
# kogato iskame da ni izleze konkretna forma s popylneni veche danni
# da gi edit-nem, izpolzvame instance


def edit_profile(request, pk, slug):

    # (re)creation of slugs
    all_profiles = Profile.objects.all()
    for p in all_profiles:
        p.slug = slugify(p.profile_name)
    Profile.objects.bulk_update(all_profiles, ['slug'])
    # ---

    current_profile = Profile.objects.get(pk=pk)

    if request.method == 'GET':
        form = ProfileEditForm(instance=current_profile)
    else:
        form = ProfileEditForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': current_profile,   # za da vzemem pk v url vyv form v html-a
    }
    return render(request, 'edit_profile.html', context)

# --------------------------------------------------------------------------
# delete


# ToDo: hide form in delete like in the exam prep2
def delete_profile(request, pk, slug):

    current_profile = Profile.objects.get(pk=pk)

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=current_profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': current_profile,
    }
    return render(request, 'delete_profile.html', context)

# --------------------------------------------------------------------------





# --------------------------------------------------------------------------

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

    # tova syshto ravoteshe na exam prep
    # album = Album.objects.filter(pk=pk) \
    #     .get()

    return specific_task


# ----------------------------------------------------------------------
# kogato iskame da ni izleze konkretna forma s popylneni veche danni
# da gi edit-nem, izpolzvame instance

# def edit_album(request, pk):
#
#     album = Album.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         form = AlbumEditForm(instance=album)
#     else:
#         form = AlbumEditForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form,
#         'album': album,   # za da vzemem pk v url vyv form v html-a
#     }
#     return render(request, 'albums/edit-album.html', context)

# ----------------------------------------------------------------------
# za delete

# def delete_album(request, pk):
#
#     album = Album.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         form = AlbumDeleteForm(instance=album)
#     else:
#         form = AlbumDeleteForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form,
#         'album': album,
#     }
#     return render(request, 'albums/delete-album.html', context)

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

