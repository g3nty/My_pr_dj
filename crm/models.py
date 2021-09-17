from django.db import models

# Create your models here.
# models.py - отвечает за работу с БД
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')#короткое-текстовое поле ChairField
    order_phone = models.CharField(max_length=200,verbose_name='Телефон')
#Потом делаем миграцию

    def __str__(self): #делам что-бы выводились имена польз. а не id с БД
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'#меняем название шапки пользователей
