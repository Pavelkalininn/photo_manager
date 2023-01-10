from django.db.models import (
    CharField,
    DateField,
    FloatField,
    ImageField,
    ManyToManyField,
    Model,
    TextField,
)


class Face(Model):
    name = CharField(
        unique=True,
        max_length=79,
        verbose_name='Имя'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Лицо'
        verbose_name_plural = 'Лица'

    def __str__(self):
        return self.name


class Photo(Model):
    image = ImageField(
        unique=True,
        verbose_name='Фото',
    )
    gps_latitude = FloatField(
        verbose_name='Широта',
        blank=True,
        null=True,
    )
    gps_longitude = FloatField(
        verbose_name='Долгота',
        blank=True,
        null=True,
    )
    names = ManyToManyField(
        Face,
        related_name='faces',
        verbose_name='Лица',
        blank=True,
        null=True,
    )
    date = DateField(
        verbose_name='Дата',
        blank=True,
        null=True,
    )
    description = TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
