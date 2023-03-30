from unittest import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from car.models import Car


class CarConsumptionFilterTestcase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        Car.objects.create(brand="Toyota", make="Corolla", year="2000-02-02", consumption=5, color="red")
        Car.objects.create(brand="Honda", make="Accord", year="2000-02-02", consumption=7, color="red")
        Car.objects.create(brand="Ford", make="F-150", year="2000-02-02", consumption=10, color="red")
        Car.objects.create(brand="Hyundai", make="i20", year="2000-02-02", consumption=4, color="red")
        Car.objects.create(brand="Aston Martin", make="Vanquish", year="2000-02-02", consumption=11, color="red")
        Car.objects.create(brand="Porsche", make="911", year="2000-02-02", consumption=14, color="red")
        Car.objects.create(brand="Fiat", make="500", year="2000-02-02", consumption=3, color="red")
        Car.objects.create(brand="Mini", make="Cooper", year="2000-02-02", consumption=9, color="red")

    def test_url_exists(self):
        response = self.client.get("/car/car/")

        self.assertEqual(response.status_code, 200)

    def test_count_correctly_returned(self):
        response = self.client.get("/car/car/")

        self.assertEqual(len(response.data), 8)

    def test_filter_correctly_returned(self):
        response = self.client.get("/car/car/?consumption__gt=9")

        self.assertEqual(len(response.data), 3)

