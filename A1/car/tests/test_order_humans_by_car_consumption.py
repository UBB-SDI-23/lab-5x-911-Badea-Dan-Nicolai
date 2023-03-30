from rest_framework.test import APIRequestFactory, APITestCase
from car.models import Car, Human


class HumansByAvgCarConsumptionTestcase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Human.objects.create(cnp="123456789", gender="m", dob="2000-02-02", email="firstname.lastname@gmail.com",
                             name="Someone_1")
        Car.objects.create(owner_id=1, brand="Toyota", make="Corolla", year="2000-02-02", consumption=5, color="red")
        Car.objects.create(owner_id=1, brand="Honda", make="Accord", year="2000-02-02", consumption=7, color="red")

        Human.objects.create(cnp="123456789", gender="m", dob="2000-02-02", email="firstname.lastname@gmail.com",
                             name="Someone_2")
        Car.objects.create(owner_id=2, brand="Ford", make="F-150", year="2000-02-02", consumption=15, color="red")
        Car.objects.create(owner_id=2, brand="Hyundai", make="i20", year="2000-02-02", consumption=4, color="red")
        Car.objects.create(owner_id=2, brand="Aston Martin", make="Vanquish", year="2000-02-02", consumption=11,
                           color="red")

        Human.objects.create(cnp="123456789", gender="m", dob="2000-02-02", email="firstname.lastname@gmail.com",
                             name="Someone_3")
        Car.objects.create(owner_id=3, brand="Porsche", make="911", year="2000-02-02", consumption=14, color="red")
        Car.objects.create(owner_id=3, brand="Fiat", make="500", year="2000-02-02", consumption=3, color="red")
        Car.objects.create(owner_id=3, brand="Mini", make="Cooper", year="2000-02-02", consumption=9, color="red")

    def test_url_exists(self):
        response = self.client.get("/car/human/by-avg-consumption/")

        self.assertEqual(response.status_code, 200)

    def test_humans_by_avg_consumption_of_cars(self):
        response = self.client.get("/car/human/by-avg-consumption/")

        self.assertEqual(len(response.data), 3)
        first = response.data[0]
        second = response.data[1]
        third = response.data[2]
        self.assertEqual(first['name'], "Someone_1")
        self.assertEqual(second['name'], "Someone_3")
        self.assertEqual(third['name'], "Someone_2")
