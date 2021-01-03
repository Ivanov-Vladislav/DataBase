from django.contrib import admin
from .models import Human, Task1

admin.site.register(Human)
admin.site.register(Task1)
admin.site.site_header = 'Управление сайтом "Todo"'