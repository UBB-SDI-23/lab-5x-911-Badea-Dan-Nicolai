from django.urls import path
from .views import CarList, CarDetail, HumanList, HumanDetail, CompetitionList, CompetitionDetail, CanCompeteDetail, \
    CanCompeteList, CarsByAvgCompetitionPrize, HumansByAvgNoOfCars, CompetitionCancompeteCreateView, \
    CarCancompeteCreateView

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('car/', CarList.as_view()),
    path('car/<int:pk>/', CarDetail.as_view()),
    path('human/', HumanList.as_view()),
    path('human/<int:pk>/', HumanDetail.as_view()),
    path('competition/', CompetitionList.as_view()),
    path('competition/<int:pk>/', CompetitionDetail.as_view()),
    path('cancompete/', CanCompeteList.as_view()),
    path('cancompete/<int:pk>/', CanCompeteDetail.as_view()),
    path('cancompete/by-avg-competition-prize/', CarsByAvgCompetitionPrize.as_view()),
    path('human/by-avg-consumption/', HumansByAvgNoOfCars.as_view()),
    path('car/<int:car_id>/competition/', CompetitionCancompeteCreateView.as_view()),
    path('competition/<int:competition_id>/car/', CarCancompeteCreateView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]