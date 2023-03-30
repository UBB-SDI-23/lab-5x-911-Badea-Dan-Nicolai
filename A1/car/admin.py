from django.contrib import admin

from .models import Car
from .models import Human
from .models import Competition
from .models import CanCompete

admin.site.register(Car)
admin.site.register(Human)
admin.site.register(Competition)
admin.site.register(CanCompete)
