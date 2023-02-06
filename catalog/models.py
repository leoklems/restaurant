from django.db import models


class MenuCategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.upper()


class MenuClassModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.upper()


class MenuModel(models.Model):
    TYPE = (('food', 'FOOD'), ('drink', 'DRINK'))
    menu_type = models.CharField(max_length=20, choices=TYPE)
    menu_class = models.ManyToManyField(MenuClassModel, blank=True)
    category = models.ForeignKey(MenuCategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    key = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/menu')
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name.upper()
