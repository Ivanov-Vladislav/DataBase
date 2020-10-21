from django.contrib import admin
from .models import Task, Human

admin.site.register(Task)
admin.site.register(Human)
admin.site.site_header = 'Управление сайтом "Chicony-IVV"'