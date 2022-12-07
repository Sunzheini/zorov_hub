from django.urls import path
from zorov_hub.main_app.views import index, games, shopping_list, \
    process_description, control_of_garden, control_of_home, chat, tasks

urlpatterns = (
    # http://127.0.0.1:8000/
    path('', index, name='index'),

    # http://127.0.0.1:8000/games/
    path('games/', games, name='games'),

    # http://127.0.0.1:8000/shopping-list/
    path('shopping-list/', shopping_list, name='shopping list'),

    # http://127.0.0.1:8000/tasks/
    path('tasks/', tasks, name='tasks'),

    # http://127.0.0.1:8000/control-of-garden/
    path('control-of-garden/', control_of_garden, name='control of garden'),

    # http://127.0.0.1:8000/control-of-home/
    path('control-of-home/', control_of_home, name='control of home'),

    # http://127.0.0.1:8000/chat/
    path('chat/', chat, name='chat'),

    # http://127.0.0.1:8000/3/process_description/
    path('<int:process_id>/process_description/', process_description, name='process-map'),
)

# http://127.0.0.1:8000/3/process_description/11asd
# 404
