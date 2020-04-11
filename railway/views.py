from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Way
from .util import *
from .forms import WayForm
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
            'ways' : page,
            'is_paginated': is_paginated,
            'next_url':next_url,
            'prev_url':prev_url
            }
    return render(request,'railway/start_page.html', context= context)

class TrainView(View):
    model = WayForm
    template = 'railway/post_create_form.html'
    raise_exception=True

"""
class PostCreate(LoginRequiredMixin,GetMix_Create,View):
    model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True 
    
    
class TagCreate(LoginRequiredMixin,GetMix_Create,View):
    model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class PostEdit(LoginRequiredMixin,GetMix_Edit,View):
    model = Post
    model_form = PostForm
    template = 'blog/post_edit.html'
    raise_exception = True


class TagEdit(LoginRequiredMixin,GetMix_Edit,View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_edit.html'
    raise_exception = True


class PostClear(LoginRequiredMixin,GetMix_Clear,View):
    model = Post 
    template = 'blog/delete_form.html'
    template_1 = 'page1'
    raise_exception = True


class TagClear(LoginRequiredMixin,GetMix_Clear,View):
     model = Tag 
     template = 'blog/delete_form.html'
     template_1 = 'tags_page'
     raise_exception = True


class post_detail(GetMix,View):
    model=Post
    template='blog/post_detail.html'


def tags_page(request):
    tags=Tag.objects.all()
    return render(request,'blog/tags_page.html',context={'tags':tags})


class tag_detail(GetMix,View):
     model=Tag
     template='blog/tag_detail.html'




def tag_list(request):
    tags = Tag.objects.all()
    return render(request,'blog/tag_list.html',context={'tags':tags})
"""