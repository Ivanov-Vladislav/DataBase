# Generated by Django 3.1.3 on 2021-01-07 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210107_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='avatar',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
