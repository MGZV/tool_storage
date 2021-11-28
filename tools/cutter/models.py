from django.db import models
from django.urls import reverse


class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    holder = models.ForeignKey('Holder', on_delete=models.PROTECT, verbose_name="Holder")
    holder_amount = models.IntegerField()
    insert = models.ManyToManyField('Insert', on_delete=models.PROTECT, verbose_name="Insert")
    insert_amount = models.IntegerField()

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = 'Worker/Storage'
        verbose_name_plural = 'Storage list'
        ordering = ['id']


class Insert(models.Model):
    name = models.CharField(max_length=255, verbose_name="Обозначение ISO")
    coating = models.CharField(max_length=255, verbose_name="Сплав")
    amount = models.IntegerField()
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пластина'
        verbose_name_plural = 'Пластины'
        ordering = ['id']


class Professions(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Профессия")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Станок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Holder(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Державка")
    holder_number = models.IntegerField()
    holder = models.ManyToManyField('Holder', on_delete=models.PROTECT, verbose_name="Державка")

    def __str__(self):
        return self.name
