# Generated by Django 3.0.2 on 2020-02-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0030_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='slug', max_length=200),
        ),
    ]
