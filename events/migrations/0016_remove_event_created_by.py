# Generated by Django 3.0.2 on 2020-02-06 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_remove_event_updated_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_by',
        ),
    ]
