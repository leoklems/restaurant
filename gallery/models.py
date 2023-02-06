from django.db import models
from django.contrib.auth.models import User


class GalleryModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='images/gallery')
