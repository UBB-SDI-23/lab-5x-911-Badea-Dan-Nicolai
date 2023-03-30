import django_filters.rest_framework
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Avg
from django.db.models import Count
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer, OneCarSerializer

from .models import Human
from .serializers import HumanSerializer, OneHumanSerializer, StatisticHumanSerializer

from .models import Competition
from .serializers import CompetitionSerializer, OneCompetitionSerializer

from .models import CanCompete
from .serializers import CanCompeteSerializer, CompetitionCancompeteSerializer, CarCancompeteSerializer


class CarList(generics.ListCreateAPIView):

    queryset = Car.objects.all()

    serializer_class = CarSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = {'consumption': ["gt", "lt"]}


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OneCarSerializer

    queryset = Car.objects.all()


class HumanList(generics.ListCreateAPIView):
    serializer_class = HumanSerializer

    def get_queryset(self):
        queryset = Human.objects.all()
        return queryset


class HumanDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OneHumanSerializer

    queryset = Human.objects.all()


class CompetitionList(generics.ListCreateAPIView):
    serializer_class = CompetitionSerializer

    def get_queryset(self):
        queryset = Competition.objects.all()
        return queryset


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OneCompetitionSerializer

    queryset = Competition.objects.all()


class CanCompeteList(generics.ListCreateAPIView):
    serializer_class = CanCompeteSerializer

    def get_queryset(self):
        queryset = CanCompete.objects.all()
        return queryset


class CanCompeteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CanCompeteSerializer

    queryset = CanCompete.objects.all()


class CarsByAvgCompetitionPrize(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        query = Car.objects\
            .annotate(avg_prize=Avg('cancompete__competition__prize'))\
            .order_by('avg_prize')
        #print(query.query)

        return query


class HumansByAvgNoOfCars(generics.ListAPIView):
    serializer_class = HumanSerializer

    def get_queryset(self):
        query = Human.objects\
            .annotate(avg_consumption = Avg('car__consumption'))\
            .order_by('avg_consumption')

        return query


class CompetitionCancompeteCreateView(generics.CreateAPIView):
    serializer_class = CompetitionCancompeteSerializer
    queryset = CanCompete.objects.all()

    def get(self, request, *args, **kwargs):
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        data_set = request.data

        car_id = kwargs['car_id']
        for elem in data_set:
            competition = elem['competition']
            competition_id = competition
            buy_in = elem['buy_in']
            sponsor = elem['sponsor']

            cancompete = CanCompete.objects.create(
                car_id=car_id, competition_id=competition_id, buy_in=buy_in, sponsor=sponsor)

        return Response({
            'competition': competition,
            'cancompete': cancompete.id
        })


class CarCancompeteCreateView(generics.CreateAPIView):
    serializer_class = CarCancompeteSerializer
    queryset = CanCompete.objects.all()

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        data_set = request.data

        competition_id = kwargs['competition_id']
        for elem in data_set:
            print(elem)
            car = elem['car']
            print(car)
            car_id = car
            buy_in = elem['buy_in']
            sponsor = elem['sponsor']

            cancompete = CanCompete.objects.create(
                car_id=car_id, competition_id=competition_id, buy_in=buy_in, sponsor=sponsor)


        return Response({
            'car': car,
            'cancompete': cancompete.id
        })
