from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
# Create your models here.

TICKET_PLACE_CHOICES = [
    ('Зг', 'Загальний'),
    ('Пк', 'Плацкартний'),
    ('Кп', 'Купейний'),
    ('Св', 'СВ'),
    ('Лк', 'Люкс'),
    ('Св', 'СВ'),
]

TICKET_SERVICES_CHOICES = [
    (' ', ' '),
    ('Пб', 'Постільна білизна'),
    ('Вд', 'Вода'),
    ('Гн', 'Гарячі напої'),
]

TICKET_CARRIAGE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
]

TICKET_TYPE_OF_TICKET_CHOICES = [
    ('1', '1'),('2', '2'),('3', '3'),('4', '4'),
    ('5', '5'),('6', '6'),('7', '7'),('8', '8'),
    ('9', '9'),('10', '10'),('11', '11'),('12', '12'),
    ('13', '13'),('14', '14'),('15', '15'),('16', '16'),
    ('17', '17'),('18', '18'),('19', '19'),('20', '20'),
    ('21', '21'),('22', '22'),('23', '23'),('24', '24'),
    ('25', '25'),('26', '26'),('27', '27'),('28', '28'),
    ('29', '29'),('30', '30'),('31', '31'),('32', '32'),
    ('33', '33'),('34', '34'),('35', '35'),('36', '36'),
    ('37', '37'),('38', '38'),('39', '39'),('40', '40')
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
    place_type=models.CharField(max_length=20,verbose_name="Тип вагону", choices=TICKET_PLACE_CHOICES)
    first=models.DateTimeField(default=None,auto_now=False,verbose_name="Дата прибуття")
    carriage=models.IntegerField(default=None,verbose_name="Номер вагону", choices=TICKET_CARRIAGE_CHOICES)
    service=models.CharField(max_length=20,default=None,verbose_name="Послуги", choices=TICKET_SERVICES_CHOICES)
    number_of_place=models.IntegerField(default=None,verbose_name="Номер місця", choices=TICKET_TYPE_OF_TICKET_CHOICES)
    type_of_ticket=models.CharField(max_length=20,verbose_name="Тип квитка", choices=TICKET_TYPE_CHOICES)

    def __str__(self):
        return f'{self.destination} {self.date_purchase}'

    #функція для підготовки квитка до завантаження
    def get_ticket_info_text(self):
        pass
