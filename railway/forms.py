from django import forms
from .models import Way,Train,Station, Ticket, TICKET_SERVICES_CHOICES, TICKET_TYPE_CHOICES
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField



class WayForm(forms.ModelForm):
    train=forms.ModelChoiceField(queryset=Train.objects.all(),required=False, widget=forms.Select()),
    stations=forms.ModelMultipleChoiceField(queryset=Station.objects.all(),required=False, widget=forms.Select()),

    class Meta:
        model = Way
        fields = ["name",
                  "train",
                  "stations",]

        widgets = {
                'name':forms.TextInput(attrs={'class':'form-control'}),
                #'train': forms.SelectMultiple(attrs={'class':'form-control'}), 
                #'stations': forms.SelectMultiple(attrs={'class':'form-control'}),
                }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('slug may not be create!!!')
            if Tag.objects.filter(slug__iexact=new_slug).count():
                raise ValidationError('This slug already extends. Please write another'.format(new_slug))
            return new_slug

class StationForm(forms.ModelForm):
    station_name = forms.CharField(max_length=32),
    departure = forms.DateTimeField(),
    arival = forms.DateTimeField(),

    class Meta:
        model = Station
        fields = ["station_name",
                  "departure",
                  "arival",]

        widgets = {
                'station_name':forms.TextInput(attrs={'class':'form-control'}),
                'departure':forms.DateTimeInput(attrs={'class':'form-control'}),
                'arival':forms.DateTimeInput(attrs={'class':'form-control'}),
                }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('slug may not be create!!!')
            if Tag.objects.filter(slug__iexact=new_slug).count():
                raise ValidationError('This slug already extends. Please write another'.format(new_slug))
            return new_slug

class TicketForm(forms.ModelForm):
    number = forms.CharField(max_length=20)
    price = forms.IntegerField()
    destination = forms.ModelChoiceField(queryset=Way.objects.all(), required=False, widget=forms.Select())
    date_purchase = forms.DateField(widget = forms.SelectDateWidget())
    first = forms.DateField(widget = forms.SelectDateWidget())
    carriage = forms.CharField(max_length=20)
    service = forms.ChoiceField(choices=TICKET_SERVICES_CHOICES)
    number_of_place = forms.IntegerField()
    type_of_ticket = forms.ChoiceField(choices=TICKET_TYPE_CHOICES)
    place_type = forms.CharField(max_length=20)
    

    class Meta:
        model = Ticket
        fields = ["number",
                  "price",
                  "destination",
                  "date_purchase",
                  "first",
                  "carriage",
                  "service",
                  "number_of_place",
                  "type_of_ticket",
                  "place_type"]

        widgets = {
                'number':forms.TextInput(attrs={'class':'form-control'}),
                'price':forms.NumberInput(attrs={'class':'form-control'}),
                }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('slug may not be create!!!')
            if Tag.objects.filter(slug__iexact=new_slug).count():
                raise ValidationError('This slug already extends. Please write another'.format(new_slug))
            return new_slug
