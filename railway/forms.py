from django import forms
from .models import Way,Train,Station
from django.core.exceptions import ValidationError



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
    
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','body','tags']

        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}), 
                'slug':forms.TextInput({'class':'form-control'}),
                'body':forms.Textarea({'class':'form-control'}),
                'tags':forms.SelectMultiple({'class':'form-control'})
                }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()
           
            if new_slug == 'create':
                raise ValidationError('slug may not be create!')
            return new_slug

"""
