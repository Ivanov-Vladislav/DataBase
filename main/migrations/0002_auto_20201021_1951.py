# Generated by Django 3.1.2 on 2020-10-21 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задача'},
        ),
        migrations.AddField(
            model_name='task',
            name='difficulty',
            field=models.CharField(default=0, max_length=10, verbose_name='Сложность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='num_people',
            field=models.CharField(default=0, max_length=2, verbose_name='Количество людей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.CharField(default=0, max_length=10, verbose_name='Время выполнения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
    ]
