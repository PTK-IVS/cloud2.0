from django.db import models


class Object(models.Model):
    object = models.IntegerField("Номер объекта")
    name = models.CharField("Имя объекта", max_length=128)
    enabled = models.BooleanField("Обслуживание")
    lat = models.FloatField("Долгота")
    lon = models.FloatField("Широта")
    trek = models.IntegerField("Трек")
    moved = models.BooleanField("Движимый")
    connection_type = models.IntegerField("Тип соединения")
    image_map = models.IntegerField("Номер изображения")


    def __str__(self):
        return self.object

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class MessageETHContactID(models.Model):
    message = models.CharField("Сообщение", max_length=128)
    user = models.IntegerField("Номер пользователя")
    uid = models.IntegerField("Идентификатор объекта")
    object = models.IntegerField("Номер объекта")
    type = models.IntegerField("Тип объекта")
    code = models.IntegerField("Адемко Код")
    section = models.IntegerField("Номер секции")
    area = models.IntegerField("Номер зоны")
    time_stamp = models.TimeField("Время")

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class AdemcoCode(models.Model):
    contact_code = models.IntegerField("Код"),
    text_code = models.TextField("Текст", max_length=128),
    message_type = models.IntegerField("Тип")

    def __str__(self):
        return self.contact_code

    class Meta:
        verbose_name = "Код"
        verbose_name_plural = "Коды"
