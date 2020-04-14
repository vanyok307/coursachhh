from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Train, Way, Station, Ticket
from .util import *
from .forms import WayForm, StationForm, TicketForm
# Create your views here.



def start_page(request):
    list = Way.objects.all() #=====
    paginator = Paginator(list,1)
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
            'ways' : list,
            'is_paginated': is_paginated,
            'next_url':next_url,
            'prev_url':prev_url
            }
    return render(request,'railway/start_page.html', context= context)

class TrainView(View):
    model = Way
    template = 'railway/post_create_form.html'
    raise_exception=True

    def get(self,request,id):
        try:
            object = Way.objects.get(id=id)
            context = {
                'ways' : object,
                        }
            return render(request,'railway/way_page.html', context=context)
        except Way.DoesNotExist:
            return start_page(request)

class WayView(View):
    def get(self, request, id):
        way = Way.objects.get(id=id)
        return render(request, 'railway/way_page.html', context={'way': way})

class WayCreateView(View):
    def get(self, request):
        waycreate = WayForm()
        return render(request, 'railway/way_create_form.html', context={'waycreate':waycreate} )

class StationView(View):
    def get(self, request, id):
        station = Station.objects.get(id=id)
        return render(request, 'railway/station_page.html', context={'statiom': station})

class StationCreateView(View):
    def get(self, request):
        stationcreate=StationForm()
        return render(request, 'railway/station_create_form.html', context={'stationcreate':stationcreate})

class TicketView(View):
    def get(self, request, id):
        ticket=Ticket.objects.get(id=id)
        return render(request, 'railway/ticket_page.html', context={'ticket': ticket})

class TicketCreateView(View):
    def get(self,request):
        ticketcreate=TicketForm()
        return render(request, 'railway/ticket_create_form.html', context={'ticketcreate': ticketcreate } )