from django.db import models
from django.utils.timezone import now


# Create your models here.

from django.db import models
from django.utils.timezone import now

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founded_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class CarModel(models.Model):
    CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('SPORT', 'Sport'),
    )

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:
    def __init__(self, id, name, city, state, zip, address, lat, long):
        self.id = id
        self.name = name
        self.city = city
        self.state = state
        self.zip = zip
        self.address = address
        self.lat = lat
        self.long = long

# Create a plain Python class `DealerReview` to hold review data

class DealerReview:
    def __init__(self, id, name, dealership, rating, review):
        self.id = id
        self.name = name
        self.dealership = dealership
        self.rating = rating
        self.review = review
