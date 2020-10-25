from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=20)
    time = models.CharField('Время выполнения', max_length=15)
    difficulty = models.CharField('Сложность', max_length=15)
    num_people = models.CharField('Количество людей', max_length=2)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Human(models.Model):
    Surname = models.CharField('Имя', max_length=20)
    Forename = models.CharField('Фамилия', max_length=20)
    age = models.CharField('Возраст', max_length=2)
    evulation_work = models.CharField('Качество работы', max_length=20)

    def __str__(self):
        return self.Surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


