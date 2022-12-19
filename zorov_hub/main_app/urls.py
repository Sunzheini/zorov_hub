from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from zorov_hub.main_app.views import index, games, shopping_list, \
    process_description, chat, \
    tasks, game_details, ControlView, ControlView2, add_profile, \
    edit_profile, delete_profile

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', index, name='index'),

    path('profile/', include([
        # http://127.0.0.1:8000/profile/add
        path('add/', add_profile, name='add profile'),
        # http://127.0.0.1:8000/profile/edit
        path('edit/', edit_profile, name='edit profile'),
        # http://127.0.0.1:8000/profile/delete
        path('delete/', delete_profile, name='delete profile'),
    ])),

    # http://127.0.0.1:8000/games/
    path('games/', games, name='games'),

    # http://127.0.0.1:8000/games/1/tetris/
    # http://127.0.0.1:8000/games/2/wow/
    path('games/<int:pk>/<slug:slug>/', game_details, name='game details'),

    # http://127.0.0.1:8000/shopping-list/
    path('shopping-list/', shopping_list, name='shopping list'),

    # http://127.0.0.1:8000/tasks/
    path('tasks/', tasks, name='tasks'),

    # http://127.0.0.1:8000/control-of-garden/
    path('control-of-garden/', ControlView.get_view1(), name='control of garden'),

    # http://127.0.0.1:8000/control-of-home/
    path('control-of-home/', ControlView2.as_view(), name='control of home'),

    # http://127.0.0.1:8000/chat/
    path('chat/', chat, name='chat'),

    # http://127.0.0.1:8000/3/process_description/
    path('<int:process_id>/process_description/', process_description, name='process-map'),
]

# http://127.0.0.1:8000/3/process_description/11asd
# 404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
