from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Way
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
    model = Train
    template = 'railway/post_create_form.html'
    raise_exception=True

    def get(self,request,id):
        try:
            object = Train.objects.get(id=id)
            context = {
                    'train' : object,
                        }
            return render(request,'railway/train_page.html', context=context)
        except Train.DoesNotExist:
            return start_page(request)

class WayView(View):
    def get(self, request, id):
        ways = Way.objects.get(id=id)
        ticket = Ticket.objects.get(destination=ways)
        return render(request, 'railway/way_page.html', context={'ways': ways,'ticket':ticket})

class WayCreateView(View,GetMix_Create,LoginRequiredMixin):
    model_form= WayForm
    template = 'railway/way_create.html'
    def get(self, request):
        form = WayForm()
        return render(request,'railway/way_create.html', context={'form':form})

    def post(self, request):
        form = WayForm(request.POST)
        if form.is_valid():
            new_way = form.save()
            return render(request, 'railway/way_create.html',context={'ways':new_way})
        return render(request,'railway/way_create.html',context={'form':form})

class WayEditView(View):
     model_form = WayForm
     template = 'railway/way_edit.html'

     def get(self, request, id):
        way = Way.objects.get(id=id)
        form = WayForm(instance=way)
        return render(request, 'railway/way_edit.html', context={'form': form, 'way': way})

     def post(self, request, id):
        way = Way.objects.get(id=id)
        form = WayForm(request.POST, instance=way)
        if form.is_valid():
            new_way = form.save()
            return render(request, 'railway/start_page.html')
        return render(request, 'railway/way_edit.html', context={'form': form})

class StationView(View):
    def get(self, request, id):
        stations = Station.objects.get(id=id)
        return render(request, 'railway/station_page.html', context={'stations': stations})

class StationCreateView(View,GetMix_Create,LoginRequiredMixin):
    model_form= StationForm
    template = 'railway/station_create.html'
    def get(self, request):
        form = StationForm()
        return render(request,'railway/station_create.html', context={'form':form})

    def post(self, request):
        form = StationForm(request.POST)
        if form.is_valid():
            new_station = form.save()
            return render(request, 'railway/station_create.html',context={'station':new_station})
        return render(request,'railway/station_create.html',context={'form':form})

class StationEditView(View):
    model_form = StationForm
    template = 'railway/station_edit.html'

    def get(self, request, id):
        station = Station.objects.get(id=id)
        form = StationForm(instance=station)
        return render(request, 'railway/station_edit.html', context={'form': form, 'station': station})

    def post(self, request, id):
        station = Station.objects.get(id=id)
        form = StationForm(request.POST, instance=station)
        if form.is_valid():
            new_station = form.save()
            return render(request, 'railway/start_page.html')
        return render(request, 'railway/station_edit.html', context={'form': form})
""""
class TicketView(View):
    def get(self, request, id):
        tickets=Ticket.objects.get(id=id)
        return render(request, 'railway/ticket_page.html', context={'tickets': tickets})
        
        
"""
class TicketCreateView(View,GetMix_Create,LoginRequiredMixin):
    model_form= TicketForm
    template = 'railway/ticket_create.html'
    def get(self, request):
        form = TicketForm()
        return render(request,'railway/ticket_create.html', context={'form':form})

    def post(self, request):
        form = TicketForm(request.POST)
        if form.is_valid():
            new_ticket = form.save()
            return render(request, 'railway/ticket_create.html',context={'ticket':new_ticket})
        return render(request,'railway/ticket_create.html',context={'form':form})
""""
class TicketDeleteView(View):
    model_form = TicketForm
    template = 'railway/ticket_delete.html'

    def get(self, request):
        form = TicketForm()
        return render(request, 'railway/ticket_delete.html', context={'form': form})

    def post(self, request):
        form = TicketForm(request.POST)
        ticket_delete = form.delete()
        return redirect(reverse, 'railway/ticket_page.html', context={'ticket': ticket_delete})
"""
