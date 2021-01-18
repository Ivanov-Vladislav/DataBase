from django.contrib import admin
from .models import person, Task1, status, branch, team, team_person

admin.site.register(person)
admin.site.register(Task1)
admin.site.register(status)
admin.site.register(branch)
admin.site.register(team)
admin.site.register(team_person)
admin.site.site_header = 'Управление сайтом "Todo"'