from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tasks', views.tasks, name='tasks'),
    path('createtask', views.createtask, name='createtask'),
    path('id_performing_person/<todo_id>', views.id_performing_personTodo, name='id_performing_person'),
    path('createhuman', views.createhuman, name='createhuman'),
]
