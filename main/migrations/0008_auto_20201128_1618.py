# Generated by Django 3.1.3 on 2020-11-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_human'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.CharField(max_length=15, verbose_name='Описание'),
        ),
    ]