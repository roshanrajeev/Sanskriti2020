# Generated by Django 3.0.2 on 2020-02-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20200206_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
