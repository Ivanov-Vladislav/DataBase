from django.db import models


class Task(models.Model):
    name = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=45)
    date = models.CharField('Дата', max_length=15)
    id_person = models.CharField('Создатель', max_length=20)
    id_status = models.CharField('Статус', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
