from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tasks', views.tasks, name='tasks'),
    path('createtask', views.createtask, name='createtask'),
    path('id_up_status/<todo_id>', views.id_up_status, name='id_up_status'),
    path('id_down_status/<todo_id>', views.id_down_status, name='id_down_status'),
    path('createhuman', views.createhuman, name='createhuman'),
    path('profile', views.profile, name='profile'),
    path('delete_task/<id>', views.delete_task, name='delete_task'),
    path('edit/<int:id>/', views.edit),
    path('edit_avatar/', views.edit_avatar),
    path('edit_data/', views.edit_data),
    path('create_person_team/', views.create_person_team),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)