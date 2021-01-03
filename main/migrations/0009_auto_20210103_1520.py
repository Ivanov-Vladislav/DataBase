# Generated by Django 3.1.3 on 2021-01-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210103_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.CharField(max_length=15, verbose_name='Описание')),
                ('date', models.DateTimeField()),
                ('id_person', models.CharField(max_length=2, verbose_name='Выполнитель')),
                ('id_status', models.TextField(verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(),
        ),
    ]