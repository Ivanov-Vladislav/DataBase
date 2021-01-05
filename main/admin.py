from django.contrib import admin
from .models import Human, Task1, status, branch

admin.site.register(Human)
admin.site.register(Task1)
admin.site.register(status)
admin.site.register(branch)
admin.site.site_header = 'Управление сайтом "Todo"'