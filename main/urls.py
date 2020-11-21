from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks', views.tasks, name='tasks'),
    path('createtask', views.createtask, name='createtask'),
    path('sign-in', views.signIn, name='sign-in'),
    path('sign-up', views.signUp.as_view(), name='sign-up'),
]
