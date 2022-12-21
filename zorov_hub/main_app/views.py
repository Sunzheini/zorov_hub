import random
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from zorov_hub.main_app.forms import NameForm, GameForm, ProfileForm, ProfileEditForm, ProfileDeleteForm, \
    TaskForm, TaskEditForm, TaskDeleteForm
from zorov_hub.main_app.models import Groceries, Tasks, Games, Profile


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


# Index function based view
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# profile / no profile different homepage

def get_profile():
    try:
        return Profile.objects.filter(pk=5).get()  # ToDo: Authentication (now looks for a profile with pk=5)
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
    return render(request, 'profile/add_profile.html', context)


# @login_required(login_url='add profile')
@login_required     # login url se podava v settings.py
def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'profiles': Profile.objects.all(),
    }

    return render(request, 'index.html', context)


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

    # current_profile = Profile.objects.get(pk=pk)
    current_profile = Profile.objects.filter(pk=pk).get()

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
    return render(request, 'profile/edit_profile.html', context)

# --------------------------------------------------------------------------
# delete


# ToDo: hide form in delete like in the exam prep2
def delete_profile(request, pk, slug):

    # current_profile = Profile.objects.get(pk=pk)
    current_profile = Profile.objects.filter(pk=pk).get()

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
    return render(request, 'profile/delete_profile.html', context)


# --------------------------------------------------------------------------
# tasks

def tasks(request):
    context = {
        'tasks_list': Tasks.objects.all(),
    }
    return render(request, 'task/tasks.html', context)


def add_task(request):

    if request.method == 'GET':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form,
    }

    return render(request, 'task/add_task.html', context)


def edit_task(request, pk):
    # current_task = Tasks.objects.get(pk=pk)
    current_task = Tasks.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = TaskEditForm(instance=current_task)
    else:
        form = TaskEditForm(request.POST, instance=current_task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form,
        'task': current_task,   # za da vzemem pk v url vyv form v html-a
    }
    return render(request, 'task/edit_task.html', context)


def delete_task(request, pk):

    # current_task = Tasks.objects.get(pk=pk)
    current_task = Tasks.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = TaskDeleteForm(instance=current_task)
    else:
        form = TaskDeleteForm(request.POST, instance=current_task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form,
        'task': current_task,
    }
    return render(request, 'task/delete_task.html', context)


# --------------------------------------------------------------------------

# add spaceships
def games(request):

    # (re)creation of slugs
    all_games = Games.objects.all()
    for g in all_games:
        g.slug = slugify(g.game_name)
    Games.objects.bulk_update(all_games, ['slug'])
    # ---

    context = {
        'games_list': Games.objects.all(),
    }
    return render(request, 'game/games.html', context)


def game_details(request, pk, slug):
    context = {
        'current_game': get_object_or_404(Games, pk=pk, slug=slug)
    }
    return render(request, 'game/game_details.html', context)


def add_game(request):
    if request.method == 'GET':
        form = GameForm()  # ako e get syzdava formata prazna
    else:  # request.method == 'post'
        form = GameForm(request.POST, request.FILES)
        form.is_valid()  # proverka sprqmo zadadenoto v formata

    # write to db - second option
    # ---------------------------------------------------------------------
        Games.objects.create(
            **form.cleaned_data
        )
        return redirect('add game')  # ostava na syshtata stranica sled save

    # ---------------------------------------------------------------------
    context = {
        'game_form': form,
    }

    return render(request, 'game/add_game.html', context)


# groceries
# ---------------------------------------------------------------------

# only to showcase of different form elements
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


# other
# ----------------------------------------------------------------------

# app da izpolzvash telefona za kamera?
def chat(request):
    return render(request, 'chat.html')


# class-based views
# --------------------------------------------------------------------------

class ControlView:
    @classmethod
    def get_view1(cls):
        return ControlView().control_of_garden

    # mikro-kontrolerite vkyshti naglasi
    # upravlenie s url i vmesto adafruit.io + kamera ot rasp pi4
    def control_of_garden(self, request):
        return render(request, 'control_of_garden.html')


# avotmatizaciq bylgarene  / solarni paneli
class ControlView2(views.TemplateView):
    template_name = 'control_of_home.html'
    extra_context = {'some_text': 'some text...'}

    def get_context_data(self, **kwargs):
        # get super's context
        context = super().get_context_data(**kwargs)
        # add our stuff
        # just to showcase I am using games
        # ['games'] will be passed to the html like in above views
        context['games'] = Games.objects.all()
        return context
