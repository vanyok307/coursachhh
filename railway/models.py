from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
# Create your models here.


class Train(models.Model):
    name = models.CharField(max_length=20)

#головна модель, яку будемо використовувати для вього
class Way(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    first_station=models.ForeignKey("Station",blank=False)
    train=models.ForeignKey("Train",
            models=on_delete.SET_DEFAULT,default=None,
            to_field="name",null=True,blank=False)
    stations = models.ManyToMayField("Station")
    final_station=models.ForeignKey("Station",blank=False)

class Station(models.Model):
    station_name=models.CharField(max_length=32)
    departure=models.DateTimeField(auto_now=False,blank=False)
    arival=models.DateTimeField(auto_now=False,blank=False)

class Ticket(models.Model):
    number=models.CharField(max_length=20)
    price = models.IntegerField()
    date_purchase=models.DateTimeField(auto_now=True)
    destination=models.ForeignKey("Way",to_field="final_station",blank=False)

    #функція для підготовки квитка до завантаження
    def get_ticket_info_text(self):
        pass
