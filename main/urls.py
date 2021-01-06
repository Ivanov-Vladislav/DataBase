from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tasks', views.tasks, name='tasks'),
    path('createtask', views.createtask, name='createtask'),
    path('id_up_status/<todo_id>', views.id_up_status, name='id_up_status'),
    path('id_down_status/<todo_id>', views.id_down_status, name='id_down_status'),
    path('createhuman', views.createhuman, name='createhuman'),
]
