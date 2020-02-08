# Generated by Django 3.0.2 on 2020-02-06 19:46

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_auto_20200207_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(default='sans20.jpg', upload_to='post_images', verbose_name='Thumbnail'),
        ),
    ]