from django.db import models

class Task1(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание')
    date = models.CharField('Дата', max_length=10)
    id_person = models.CharField('Создатель', max_length=10)
    CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    id_status = models.CharField(max_length=300, choices = CHOICES)
    id_performing_person = models.CharField('Исполнитель', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Human(models.Model):
    Surname = models.CharField('Имя', max_length=20)
    Forename = models.CharField('Фамилия', max_length=20)
    ages = models.CharField('Возраст', max_length=2)
    evulation_work = models.CharField('Качество работы', max_length=20)

    def __str__(self):
        return self.Surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class status(models.Model):
    name = models.CharField('Наименование статуса', max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

