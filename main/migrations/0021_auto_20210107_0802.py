# Generated by Django 3.1.3 on 2021-01-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210105_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='id_branch',
            field=models.CharField(max_length=13, verbose_name='отдел разработки'),
        ),
    ]