from django.db import models
from django.contrib.auth.models import User


class BookCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.upper()


class BookModel(models.Model):
    key = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/book')
    description = models.TextField()
    category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    
    STATUS = (('available', 'AVAILABLE'), ('not available', 'NOT AVAILABLE'))
    status = models.CharField(max_length=20, choices=STATUS, blank=True, default='confirmed')

    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name.upper()
        
    def save(self, *args, **kwargs):
        self.key = self.name + self.category.name

        super(BookModel, self).save(*args, **kwargs)
        