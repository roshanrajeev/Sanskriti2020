# Generated by Django 3.0.2 on 2020-02-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0031_auto_20200207_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=200),
        ),
    ]
