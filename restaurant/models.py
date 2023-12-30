from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255)
    number_of_guests = models.IntegerField(validators=[MaxValueValidator(999999)])
    booking_date = models.DateTimeField(auto_now=True)
    
class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=10, decimal_places=2) # decimal(10,2)
    inventory = models.IntegerField(validators=[MaxValueValidator(99999)]) # int(5)