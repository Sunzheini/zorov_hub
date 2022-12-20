from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from zorov_hub.main_app.views import index, games, shopping_list, \
    chat, \
    tasks, game_details, ControlView, ControlView2, add_profile, \
    edit_profile, delete_profile, \
    add_task, edit_task, delete_task, \
    add_game

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', index, name='index'),

    path('profile/', include([
        # http://127.0.0.1:8000/profile/add/
        path('add/', add_profile, name='add profile'),
        # http://127.0.0.1:8000/profile/edit/
        path('edit/<int:pk>/<slug:slug>/', edit_profile, name='edit profile'),
        # http://127.0.0.1:8000/profile/delete/
        path('delete/<int:pk>/<slug:slug>/', delete_profile, name='delete profile'),
    ])),

    path('tasks/', include([
        # http://127.0.0.1:8000/tasks/
        path('', tasks, name='tasks'),
        # http://127.0.0.1:8000/tasks/add/
        path('add/', add_task, name='add task'),
        # http://127.0.0.1:8000/tasks/edit/
        path('edit/<int:pk>/', edit_task, name='edit task'),
        # http://127.0.0.1:8000/tasks/delete/
        path('delete/<int:pk>/', delete_task, name='delete task'),
    ])),

    path('games/', include([
        # http://127.0.0.1:8000/games/
        path('', games, name='games'),
        # http://127.0.0.1:8000/games/add/
        path('games/', add_game, name='add game'),
        # http://127.0.0.1:8000/games/2/wow/
        path('games/<int:pk>/<slug:slug>/', game_details, name='game details'),
    ])),

    # http://127.0.0.1:8000/shopping-list/
    path('shopping-list/', shopping_list, name='shopping list'),

    # http://127.0.0.1:8000/control-of-garden/
    path('control-of-garden/', ControlView.get_view1(), name='control of garden'),

    # http://127.0.0.1:8000/control-of-home/
    path('control-of-home/', ControlView2.as_view(), name='control of home'),

    # http://127.0.0.1:8000/chat/
    path('chat/', chat, name='chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
