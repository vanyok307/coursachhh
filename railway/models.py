from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
# Create your models here.


def gen_slug(s):
    new_slug = slugify(s,allow_unicode=True)
    return new_slug + '-' + str(int(time()))





class Way(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    _from=models.CharField(max_length=150,unique=False)
    train_number=models.CharField(blank=True,max_length=150,unique=True)
    to=models.TextField(blank=True,db_index=False)
    date_out=models.DateTimeField(auto_now=False)

"""
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})

    def get_edit_url(self):                         
        return reverse('post_edit',kwargs={'slug':self.slug})

    def get_clear_url(self):
        return reverse('post_clear',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args,**kwargs)
        return 

    def __str__(self):
        return self.title
"""
