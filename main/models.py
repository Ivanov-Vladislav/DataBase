from django.db import models

class status(models.Model):
    name = models.CharField('Наименование статуса', max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Task1(models.Model):
    title = models.CharField('Название', max_length=25)
    description = models.TextField('Описание')
    date = models.CharField('Дата', max_length=10)
    id_person = models.CharField('Создатель', max_length=10)
    id_status = models.ForeignKey(status,  on_delete=models.CASCADE)
    id_performing_person = models.CharField('Исполнитель', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class branch(models.Model):
    name = models.CharField('Наименование отдела', max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Human(models.Model):
    first_name = models.CharField('Имя', max_length=10)
    second_name = models.CharField('Фамилия', max_length=15)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")
    id_registarion = models.CharField('id при регистрации', max_length=5)
    id_branch = models.ForeignKey(branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

