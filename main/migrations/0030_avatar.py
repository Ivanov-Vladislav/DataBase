# Generated by Django 3.1.3 on 2021-01-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20210111_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='Имя')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
