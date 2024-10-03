from django.db import models
from django.contrib.auth.models import User


# you create your models here

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='scheduled')

    def __str__(self):
        return f"{self.client.user.username} - {self.service.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'


