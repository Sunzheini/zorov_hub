from django.contrib import admin
from zorov_hub.main_app.models import Groceries, Tasks, Games, Profile

"""
python manage.py createsuperuser
daniel
daniel_zorov@abv.bg
Maimun06
"""


@admin.register(Groceries)
class GroceriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'grocery_name', 'grocery_count')  # display v admin


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name')
    list_filter = ('task_email', 'task_accepted')
    search_fields = ('id', 'task_name')


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_name')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_name', 'profile_name')
