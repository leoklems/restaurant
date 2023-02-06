from django.db import models


# Create your models here.
class SiteInfoModel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='images/logo', null=True, blank=True)
    mobile_1 = models.CharField(max_length=20, null=True, blank=True)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=30, null=True, blank=True)
    working_hour = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


