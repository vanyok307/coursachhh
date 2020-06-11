import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from .models import Way
from .util import *
from .forms import WayForm, StationForm, TicketForm, UserForm


class UserRegView(View):
    model = User
    
    @csrf_exempt
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'user_reg.html',{'form':form})
    @csrf_exempt
    def post(self, request):
        form = UserCreationForm(request.POST)
        username = request.POST.get('email')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return render(request,'index.html')

class UserView(View):
    model = User
    
    @csrf_exempt
    def get(self, request):
        form = UserForm()
        return render(request, 'user_log.html',{'form':form})
    
    @csrf_exempt
    def post(self, request):
        form = UserForm(request.POST)
        
        if User.objects.get(username=request.POST.get('email')):
            username = request.POST.get('email')
            raw_password = request.POST.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'index.html')
        return render(request,'user_log.html',context={'form':form})

def user_view(request):
    return render(request,'user.html')

def logout_view(request):
    logout(request)
    return render(request,'index.html')

def start_page(request):
    return render(request,'index.html')

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
        return render(request, 'way_page.html', context={'ways': ways,'ticket':ticket})

class WaysView(View):

    def get(self, request):
        ways = Way.objects.filter()
        return render(request, 'way_page.html', context={'ways': ways})

class WayCreateView(View,GetMix_Create,LoginRequiredMixin):
    model_form= WayForm
    template = 'way_create.html'
    def get(self, request):
        form = WayForm()
        return render(request,'way_create.html', context={'form':form})

    def post(self, request):
        form = WayForm(request.POST)
        if form.is_valid():
            new_way = form.save()
            return render(request, 'way_create.html',context={'ways':new_way})
        return render(request,'way_create.html',context={'form':form})

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

class TicketsView(View):
    def get(self, request):
        tickets=Ticket.objects.all().filter(type_of_ticket="Повний")
        return render(request, 'ticket_page.html', context={'tickets': tickets})

class TicketFilterView(View):
    def get(self, request, destination):
        tickets=Ticket.objects.all().filter(destination=destination)
        return render(request, 'ticket_page.html', context={'tickets': tickets})

class TicketFilterStationView(View):
    def get(self, request, id):
        way=Way.objects.get(id=id)
        station = Way.stations.filter()
        tickets = Ticket.objects.filter()
        return render(request, 'ticket_page.html', context={'tickets': tickets})

def download(request, destination):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Тест.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='квиток.pdf')


        
        
