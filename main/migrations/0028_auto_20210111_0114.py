# Generated by Django 3.1.3 on 2021-01-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20210111_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task1',
            name='id_status',
            field=models.CharField(max_length=15, verbose_name='Статус'),
        ),
    ]
