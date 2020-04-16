from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
# Create your models here.

TICKET_SERVICES_CHOICES = [
    ('Пб', 'Постільна білизна'),
    ('Вд', 'Вода'),
    ('Гн', 'Гарячі напої'),
]

TICKET_TYPE_CHOICES = [
    ('Ст', 'Студентський квиток'),
    ('Пл', 'Пільговий'),
    ('Пв', 'Повний'),
]



class Train(models.Model):
    name = models.CharField(max_length=20,unique=True,verbose_name="Назва поїзду")
    
    def __str__(self):
        return self.name


#головна модель, яку будемо використовувати для вього
class Way(models.Model):
    name=models.CharField(max_length=150,unique=True,verbose_name="ім'я шляху")
    train=models.ForeignKey("Train",
            on_delete=models.SET_DEFAULT,default=None,
            to_field="name",null=True,blank=False,verbose_name="Номер поїзду")
    stations = models.ManyToManyField("Station",verbose_name="Станції")
    
    def __str__(self):
        return self.name

class Station(models.Model):
    station_name=models.CharField(max_length=32,unique=True,verbose_name="Станція")
    departure=models.DateTimeField(auto_now=False,blank=False,verbose_name="Час відʼїзду")
    arival=models.DateTimeField(auto_now=False,blank=False,verbose_name="Час прибуття")

    
    def __str__(self):
        return self.station_name


class Ticket(models.Model):
    number=models.CharField(max_length=20,verbose_name="Номер квитка")
    price = models.IntegerField(verbose_name="Ціна")
    date_purchase=models.DateTimeField(auto_now=False,verbose_name="Дата відправлення")
    destination=models.ForeignKey("Way",on_delete=models.SET_DEFAULT,default=None,null=True,to_field="name",blank=False,verbose_name="Кінцева станція")
    place_type=models.CharField(max_length=20,verbose_name="Тип вагону")
    first=models.DateTimeField(default=None,auto_now=False,verbose_name="Дата прибуття")
    carriage=models.IntegerField(default=None,verbose_name="Номер вагону")
    service=models.CharField(max_length=20,default=None,verbose_name="Послуги", choices=TICKET_SERVICES_CHOICES)
    number_of_place=models.IntegerField(default=None,verbose_name="Номер місця")
    type_of_ticket=models.CharField(max_length=20,verbose_name="Тип квитка", choices=TICKET_TYPE_CHOICES)

    def __str__(self):
        return f'{self.destination} {self.date_purchase}'

    #функція для підготовки квитка до завантаження
    def get_ticket_info_text(self):
        pass
