from cStringIO import StringIO
import os

from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage

from PIL import Image

# Thumbnail size tuple defined in an app-specific settings module - e.g. (400, 400)
from app.settings import THUMB_SIZE

class Photo(models.Model):
    """
    Photo model with automatically generated thumbnail.
    """
    photo = models.ImageField(upload_to='photos')
    thumbnail = models.ImageField(upload_to='thumbs', editable=False)

    def save(self, *args, **kwargs):
        """
        Make and save the thumbnail for the photo here.
        """
        super(Photo, self).save(*args, **kwargs)
        if not self.make_thumbnail():
            raise Exception('Could not create thumbnail - is the file type valid?')

    def make_thumbnail(self):
        """
        Create and save the thumbnail for the photo (simple resize with PIL).
        """
        fh = storage.open(self.photo.name, 'r')
        try:
            image = Image.open(fh)
        except:
            return False

        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
        fh.close()

        # Path to save to, name, and extension
        thumb_name, thumb_extension = os.path.splitext(self.photo.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = StringIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # Load a ContentFile into the thumbnail field so it gets saved
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
        temp_thumb.close()

        return True