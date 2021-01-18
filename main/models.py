from django.db import models
from datetime import date


class branch(models.Model):
    name = models.CharField('Наименование отдела', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class person(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")
    id_registarion = models.IntegerField()
    id_branch = models.ForeignKey(branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class status(models.Model):
    name = models.CharField('Наименование статуса', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Task1(models.Model):
<<<<<<< HEAD
    title = models.CharField('Название', max_length=100)
=======
    title = models.CharField('Название', max_length=50)
>>>>>>> 7b05a2506e9e04aaee2388b926d607475b0cde69
    description = models.TextField('Описание')
    date = models.DateField(("Date"), default=date.today)
    id_person = models.ForeignKey(person,  on_delete=models.CASCADE)
    id_status = models.ForeignKey(status,  on_delete=models.CASCADE)
    id_performing_person = models.CharField('Исполнитель', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Avatar(models.Model):
    title = models.CharField('Имя', max_length=10)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title


class team(models.Model):
    name = models.CharField('Название', max_length=50)
    date = models.DateField(("Date"), default=date.today)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class team_person(models.Model):
    id_team = models.ForeignKey(team, on_delete=models.CASCADE)
    id_person = models.ForeignKey(person, on_delete=models.CASCADE)