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
            'ways' : list,
            'is_paginated': is_paginated,
            'next_url':next_url,
            'prev_url':prev_url
            }
    return render(request,'railway/start_page.html', context= context)

class TrainView(View):
    model = WayForm
    template = 'railway/post_create_form.html'
    raise_exception=True
