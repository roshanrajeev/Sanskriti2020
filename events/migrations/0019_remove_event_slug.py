# Generated by Django 3.0.2 on 2020-02-06 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20200206_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
