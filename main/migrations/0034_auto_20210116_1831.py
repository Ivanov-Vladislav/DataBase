# Generated by Django 3.1.3 on 2021-01-16 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210116_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task1',
            name='id_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.human'),
        ),
    ]
