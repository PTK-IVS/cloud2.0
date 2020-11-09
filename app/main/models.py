from datetime import time

from django.db import models


class Role(models.Model):
    role: str = models.TextField(
        "Роль",
        max_length=128
    )

    def __str__(self):
        return self.role


class MessageETHContactID(models.Model):
    message: str = models.CharField(
        "Сообщение",
        max_length=128
    )
    user: int = models.IntegerField(
        "Номер пользователя"
    )
    uid: int = models.IntegerField(
        "Идентификатор объекта"
    )
    object: int = models.IntegerField(
        "Номер объекта"
    )
    type: int = models.IntegerField(
        "Тип объекта"
    )
    code: int = models.IntegerField(
        "Адемко Код"
    )
    section: int = models.IntegerField(
        "Номер секции"
    )
    area: int = models.IntegerField(
        "Номер зоны"
    )
    time_stamp: time = models.TimeField(
        "Время"
    )

    def __str__(self):
        return self.message

    class Meta:
        verbose_name: str = "Сообщение"
        verbose_name_plural: str = "Сообщения"


class Object(models.Model):
    object: int = models.OneToOneField(
        MessageETHContactID,
        on_delete=models.CASCADE
    )
    name: str = models.CharField(
        "Имя объекта",
        max_length=128
    )
    enabled: bool = models.BooleanField(
        "Обслуживание"
    )
    lat: float = models.FloatField(
        "Долгота"
    )
    lon: float = models.FloatField(
        "Широта"
    )
    trek: int = models.IntegerField(
        "Трек"
    )
    moved: bool = models.BooleanField(
        "Движимый"
    )
    connection: int = models.IntegerField(
        "Тип соединения"
    )
    image: int = models.IntegerField(
        "Номер изображения"
    )

    def __str__(self):
        return self.object

    class Meta:
        verbose_name: str = "Объект"
        verbose_name_plural: str = "Объекты"


class AdemcoCode(models.Model):
    code = models.OneToOneField(
        MessageETHContactID,
        on_delete=models.CASCADE
    )
    text_code = models.TextField(
        "Текст",
        max_length=128
    ),
    type = models.OneToOneField(
        MessageETHContactID,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Код"
        verbose_name_plural = "Коды"


class Section(models.Model):
    object = models.IntegerField(
        "Номер объекта"
    )
    name = models.CharField(
        "Имя секции",
        max_length=128
    )
    number = models.IntegerField(
        "Номер секции"
    )
    status: str = models.CharField(
        "Статус",
        max_length=128
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"


class User(models.Model):
    user: str = models.OneToOneField(
        MessageETHContactID,
        on_delete=models.CASCADE
    )
    email: str = models.EmailField(
        "Электронная почта"
    )
    password: str = models.TextField(
        "Пароль",
        max_length=128
    )
    role: Role = models.OneToOneField(
        Role,
        on_delete=models.CASCADE
    )
    phone: str = models.TextField(
        "Номер телефона",
        max_length=64
    )

    class Meta:
        verbose_name: str = "Пользователь"
        verbose_name_plural: str = "Пользователи"


class WebAddr(models.Model):
    role: int = models.IntegerField(
        "Роль"
    )
    webaddr: str = models.CharField(
        "Адрес",
        max_length=128
    )


class Status(models.Model):
    status: str = models.TextField(
        "Статус",
        max_length=256
    )


class Area(models.Model):
    section: int = models.ForeignKey(
        Section,
        on_delete=models.CASCADE
    )
    name: str = models.CharField(
        "Имя зоны",
        max_length=128
    )
    number: int = models.IntegerField(
        "Номер зоны"
    )
    object: int = models.IntegerField(
        "Объект"
    )
    status: int = models.IntegerField(
        "Статус"
    )


class DeviceAlarmStatus(models.Model):
    object: int = models.IntegerField(
        "Объект"
    )
    section: int = models.OneToOneField(
        Section,
        on_delete=models.CASCADE
    )
    area: int = models.IntegerField(
        Area
    )
    status: Status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )


class UserWithObject(models.Model):
    user: int = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    object: int = models.ForeignKey(
        Object,
        on_delete=models.CASCADE
    )


class KeyAndCode(models.Model):
    user: int = models.OneToOneField(
        UserWithObject,
        on_delete=models.CASCADE
    )
    object: int = models.OneToOneField(
        UserWithObject,
        on_delete=models.CASCADE
    )
    section: int = models.OneToOneField(
        Section,
        on_delete=models.CASCADE
    )
    code: int = models.IntegerField(
        "Код"
    )
    key: int = models.IntegerField(
        "Ключ"
    )


class JSONPolygon(models.Model):
    geoJSON: str = models.TextField(
        "ГЕО",
        max_length=256
    )
    polygon: str = models.TextField(
        "Полигон",
        max_length=256
    )

    class Meta:
        verbose_name: str = "Полигон"
        verbose_name_plural: str = "Полигоны"


class Trek(models.Model):
    trek: int = models.OneToOneField(
        Object,
        on_delete=models.CASCADE
    )
    lat: float = models.FloatField(
        "Широта"
    )
    lon: float = models.FloatField(
        "Долгота"
    )
    time_stamp: time = models.TimeField(
        "Время"
    )


class Connection(models.Model):
    connection: str = models.OneToOneField(
        Object,
        on_delete=models.CASCADE
    )


class Image(models.Model):
    file_extension: str = models.CharField(
        "Расширение",
        max_length=256
    )
    image: Object = models.OneToOneField(
        Object,
        on_delete=models.CASCADE
    )
