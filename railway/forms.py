from django import forms
from .models import Way, Station, Ticket
from django.core.exceptions import ValidationError

class WayForm(forms.ModelForm):
    queryset = Way.objects.all()

    class Meta:
        model = Way
        fields = ["name", "train_number", "stations"]

        widgets = {
                'name':forms.Textarea(attrs={'class':'form-control'}),
                'train_number':forms.ModelChoiceField(attrs={'class':'form-control'}),
                "stations":forms.ModelMultipleChoiceField(attrs={'class':'form-control'}),
                }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('slug may not be create!!!')
            if Tag.objects.filter(slug__iexact=new_slug).count():
                raise ValidationError('This slug already extends. Please write another'.format(new_slug))
            return new_slug

class StationForm(forms.ModelForm):
    queryset = Station.objects.all()

    class Meta:
         model = Station
         fields = ["station_name", "departure", "arival"]

         widgets = {
             'station_name':forms.Textarea(attrs={'class': 'form-control'}),
             'departure':forms.DateTimeField(attrs={'class': 'form-control'}),
             'arival':forms.DateTimeField(attrs={'class': 'form-control'}),
         }

         def clean_slug(self):
             new_slug = self.cleaned_data['slug'].lower()

             if new_slug == 'create':
                 raise ValidationError('slug may not be create!!!')
             if Tag.objects.filter(slug__iexact=new_slug).count():
                 raise ValidationError('This slug already extends. Please write another'.format(new_slug))
             return new_slug

class TicketForm(forms.ModelForm):
    queryset = Ticket.objects.all()

    class Meta:
        model = Ticket
        fields = ["number", "price", "date_purchase", "destination"]

        widgets = {
            'number':forms.Textarea(attrs={'class': 'form-control'}),
            'price':forms.IntegerField(attrs={'class': 'form-control'}),
            'date_purchase':forms.DateTimeField(attrs={'class': 'form-control'}),
            'destination': forms.ModelChoiceField(attrs={'class': 'form-control'}),
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('slug may not be create!!!')
            if Tag.objects.filter(slug__iexact=new_slug).count():
                raise ValidationError('This slug already extends. Please write another'.format(new_slug))
            return new_slug
