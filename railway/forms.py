from django import forms
from .models import Way
from django.core.exceptions import ValidationError

class WayForm (forms.ModelForm):
    name = forms.CharField(max_length=15)
    train_number = forms.SlugField(max_length=150)

    class Meta:
        model = Way
        fields = ["name",
                  "train_number",]

        widgets = {
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'train_number':forms.TextInput(attrs={'class':'form-control'}),
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
