from django.db import models

# Create your models here.
# models.py - отвечает за работу с БД
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')#короткое-текстовое поле ChairField
    order_phone = models.CharField(max_length=200,verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Статус")

    # order_status-создаем новое поле привязав его к классу StatusCrm(род.классу).
    # ForeignKey - поле привязки.ForeignKey(класс родителя,n_delete=models.-параметры удаления)
    #n_delete=models.(параметры удлаения) - CASCADE - когда, при удалении родидетеля удаляются все потомки,комментарии,
    #SET_NULL - при удаления поля, потомки переходят в NULL. PROTECT - запрет на удаление полей, не дает ползователям удалять поля.
    #null= True, blank=True записываем эти парамтеры т.к мы их добавили после миграции.null - для одобрения пустоты в БД
    # blank - для одобрения пустоты в полях админ панели в DJ
    def __str__(self): #делам что-бы выводились имена польз. а не id с БД
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'#меняем название шапки пользователей


class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Завка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self): #делам что-бы выводились имена польз. а не id с БД
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
