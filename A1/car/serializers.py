from rest_framework import serializers
from .models import Car
from .models import Human
from .models import Competition
from .models import CanCompete


class CarSerializer(serializers.ModelSerializer):

    avg_prize = serializers.FloatField(read_only=True)

    class Meta:
        model = Car
        fields = ('__all__')


class HumanSerializer(serializers.ModelSerializer):

    count_consumption = serializers.FloatField(read_only=True)

    class Meta:
        model = Human
        fields = ('__all__')


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('__all__')


class CanCompeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanCompete
        #depth = 1
        fields = ('__all__')


class OneHumanSerializer(serializers.ModelSerializer):
    cars = CarSerializer(source='car_set', many=True)

    class Meta:
        model = Human
        fields = ('cnp', 'gender', 'dob', 'email', 'name', 'cars')
        expandable_fields = {"car_set": (CarSerializer, {"source": "car_set"})}


class StatisticHumanSerializer(serializers.ModelSerializer):
    cars = CarSerializer(source='car_set', many=True)

    class Meta:
        model = Human
        fields = ('name', 'cars')
        expandable_fields = {"car_set": (CarSerializer, {"source": "car_set"})}


class OneCanCompeteSerializerTowardsCar(serializers.ModelSerializer):
    class Meta:
        model = CanCompete
        depth = 1
        fields = ( 'buy_in', 'car', 'sponsor')


class OneCompetitionSerializer(serializers.ModelSerializer):
    cancompete = OneCanCompeteSerializerTowardsCar(source='cancompete_set', many=True)

    class Meta:
        model = Competition
        fields = ('name', 'region', 'date', 'prize', 'category', 'cancompete')
        #fields = ('__all__')


class OneCanCompeteSerializerTowardsCompetition(serializers.ModelSerializer):
    class Meta:
        model = CanCompete
        depth = 1
        fields = ('buy_in', 'competition', 'sponsor')


class OneCarSerializer(serializers.ModelSerializer):
    cancompete = OneCanCompeteSerializerTowardsCompetition(source='cancompete_set', many=True)

    class Meta:
        model = Car
        depth = 1
        fields = ('owner', 'brand', 'make', 'year', 'consumption', 'color', 'cancompete')


class CompetitionCancompeteSerializer(serializers.Serializer):
    competition = serializers.PrimaryKeyRelatedField(queryset=Competition.objects.all())
    buy_in = serializers.IntegerField()
    sponsor = serializers.CharField(max_length=100)


class CarCancompeteSerializer(serializers.Serializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    buy_in = serializers.IntegerField()
    sponsor = serializers.CharField(max_length=100)
