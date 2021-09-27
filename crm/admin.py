from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm
#регестрация приложения в админ панелию

# Register your models here.
#регестрация приложения/класса в админ панели из models
admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
#Потом делаем миграцию