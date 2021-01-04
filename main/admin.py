from django.contrib import admin
from .models import Human, Task1, status

admin.site.register(Human)
admin.site.register(Task1)
admin.site.register(status)
admin.site.site_header = 'Управление сайтом "Todo"'