# Generated by Django 3.2.16 on 2023-01-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=79, unique=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Лицо',
                'verbose_name_plural': 'Лица',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to='', verbose_name='Фото')),
                ('gps_latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('gps_longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('names', models.ManyToManyField(blank=True, null=True, related_name='faces', to='photo.Face', verbose_name='Лица')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ('-id',),
            },
        ),
    ]
