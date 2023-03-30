from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

# sudo /home/ubuntu/anaconda3/bin/python manage.py runserver 0.0.0.0:80
# http://13.50.242.190/car/car/


class Human(models.Model):
    cnp = models.CharField(max_length=13, null=True)
    gender = models.CharField(max_length=6, null=True)
    dob = models.DateField(null=True)
    email = models.CharField(max_length=100,
                             validators=[RegexValidator(r'^[A-Za-z0-9_!#$%&\'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$',
                                                        message="Wrong email format")],
                             null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    owner = models.ForeignKey(Human, on_delete=models.CASCADE, null=True)
    brand = models.CharField(max_length=100, null=True)
    make = models.CharField(max_length=100, null=True)
    year = models.DateField(null=True)
    consumption = models.PositiveIntegerField(null=True,
                                              validators=[MaxValueValidator(50),
                                                          MinValueValidator(0)])
    color = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.brand + " " + self.make


class Competition(models.Model):
    name = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    prize = models.PositiveIntegerField(null=True,
                                              validators=[MaxValueValidator(100000000),
                                                          MinValueValidator(0)])
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class CanCompete(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True)
    buy_in = models.PositiveIntegerField(null=True)
    sponsor = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.car.brand + self.car.make} - {self.competition.name}"
