from rest_framework.test import APIRequestFactory, APITestCase
from car.models import Car, Competition, CanCompete


class CarsByAvgCompPrizeTestcase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Car.objects.create(brand="Toyota", make="Corolla", year="2000-02-02", consumption=5, color="red")
        Car.objects.create(brand="Honda", make="Accord", year="2000-02-02", consumption=7, color="red")
        Car.objects.create(brand="Ford", make="F-150", year="2000-02-02", consumption=15, color="red")
        Car.objects.create(brand="Hyundai", make="i20", year="2000-02-02", consumption=4, color="red")
        Car.objects.create(brand="Aston Martin", make="Vanquish", year="2000-02-02", consumption=11,
                           color="red")
        Car.objects.create(brand="Porsche", make="911", year="2000-02-02", consumption=14, color="red")
        Car.objects.create(brand="Fiat", make="500", year="2000-02-02", consumption=3, color="red")
        Car.objects.create(brand="Mini", make="Cooper", year="2000-02-02", consumption=9, color="red")

        Competition.objects.create(name="Goodwood", region="UK", date="2023-07-10", prize=0, category="all")
        Competition.objects.create(name="Rally", region="Worldwide", date="2023-07-10", prize=100000, category="dirt")
        Competition.objects.create(name="Endurance", region="France", date="2023-07-10", prize=500000, category="all")

        CanCompete.objects.create(car_id=1, competition_id=2, buy_in=10000, sponsor="some_sponsor")
        CanCompete.objects.create(car_id=1, competition_id=1, buy_in=0, sponsor="some_sponsor")
        CanCompete.objects.create(car_id=6, competition_id=3, buy_in=10000, sponsor="some_sponsor")
        CanCompete.objects.create(car_id=4, competition_id=2, buy_in=10000, sponsor="some_sponsor")
        CanCompete.objects.create(car_id=2, competition_id=2, buy_in=10000, sponsor="some_sponsor")
        CanCompete.objects.create(car_id=8, competition_id=2, buy_in=10000, sponsor="some_sponsor")


    def test_url_exists(self):
        response = self.client.get("/car/cancompete/by-avg-competition-prize/")

        self.assertEqual(response.status_code, 200)

    def test_cars_by_avg_comp_prize(self):
        response = self.client.get("/car/cancompete/by-avg-competition-prize/")

        self.assertEqual(len(response.data), 8)
        first = response.data[0]
        second = response.data[1]
        third = response.data[2]
        fourth = response.data[3]
        fifth = response.data[4]
        sixth = response.data[5]
        seventh = response.data[6]
        eighth = response.data[7]

        self.assertEqual(eighth['brand'], "Porsche")
        self.assertEqual(eighth['avg_prize'], 500000)

        self.assertEqual(seventh['brand'], "Mini")
        self.assertEqual(seventh['avg_prize'], 100000)

        self.assertEqual(first['brand'], "Ford")
        self.assertEqual(first['avg_prize'], None)

