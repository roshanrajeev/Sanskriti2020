# Generated by Django 3.0.2 on 2020-02-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0033_auto_20200208_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=200),
        ),
    ]
