from django.urls import path
from . import views
from django.views.generic.edit import FormView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tasks', views.tasks, name='tasks'),
    path('createtask', views.createtask, name='createtask'),
    path('createhuman', views.createhuman, name='createhuman'),
    path('sign-in', views.signIn, name='sign-in'),
]
