from django.db import models
from django.contrib.auth.models import User
import random


class TableModel(models.Model):
    name = models.CharField(max_length=100)
    minimum_guest = models.IntegerField()
    maximum_guest = models.IntegerField()
    STATUS = (('available', 'AVAILABLE'), ('reserved', 'RESERVED'), ('occupied', 'OCCUPIED'), ('maintenance', 'MAINTENANCE'))
    status = models.CharField(max_length=20, choices=STATUS, default='available')

    def __str__(self):
        return self.name.upper()
        
        
class PreferenceModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name.upper()



class ReservationModel(models.Model):
    code = models.CharField(max_length=25, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    number_of_guest = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    
    preference = models.ForeignKey(PreferenceModel, on_delete=models.SET_NULL, blank=True, null=True)
    table = models.ForeignKey(TableModel, on_delete=models.SET_NULL, blank=True, null=True)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='staff')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    STATUS = (('confirmed', 'CONFIRMED'), ('pending', 'PENDING'))
    confirmation_status = models.CharField(max_length=20, choices=STATUS, blank=True, default='confirmed')
    arrival_status = models.CharField(max_length=20, choices=STATUS, blank=True, default='pending')
    MODE = (('offline', 'OFFLINE'), ('online', 'ONLINE'))
    mode = models.CharField(max_length=20, choices=MODE, blank=True, default='offline')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.full_name.upper()
        
    def save(self, *args, **kwargs):
        if not self.code:
            while 1:
                code = str(random.choices(range(1000, 9999))[0]) + '-' + str(random.choices(range(1000, 9999))[0]) 
                code_exist = ReservationModel.objects.filter(code=code)
                if not code_exist:
                    self.code = code
                    break

        super(ReservationModel, self).save(*args, **kwargs)
