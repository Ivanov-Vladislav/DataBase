# Generated by Django 3.1.3 on 2021-01-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210103_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='task1',
            name='id_performing_person',
            field=models.CharField(default=1, max_length=10, verbose_name='Исполнитель'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task1',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task1',
            name='id_person',
            field=models.CharField(max_length=10, verbose_name='Создатель'),
        ),
    ]
