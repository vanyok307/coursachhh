from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from .models import * 

class GetMix:
    model=None
    template=None    
    
    def get(self,request,slug):
        obj=get_object_or_404(self.model,slug__iexact=slug)
        return render(request,self.template,context={ self.model.__name__.lower() : obj,'admin_object':obj,'detail': True })


class GetMix_Create:
    model=None
    template=None

    def get(self,request):
       form= self.model()
       return render(request,self.template,context={'form':form})

    def post(self,request):
        bound_form = self.model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,self.template,context={'form':bound_form})
        
class GetMix_Edit:
    model=None
    model_form=None
    template=None
    
    def get(self,request,slug):
        obj=self.model.objects.get(slug__iexact=slug)
        bound_form=self.model_form(instance=obj)
        return render(request,self.template,context={'form':bound_form,self.model.__name__.lower():obj})

    def post(self,request,slug):
        obj=self.model.objects.get(slug__iexact=slug)
        bound_form=self.model_form(request.POST,instance=obj)
        
        if bound_form.is_valid():
            new_obj=bound_form.save()
            return redirect(new_obj)
        
        return render(request,self.template,context={'form':bound_form,self.model.__name__.lower():obj})
        
class GetMix_Clear:
    model=None
    template=None
    template_1=None
    
    def get(self,request,slug):
        obj=self.model.objects.get(slug__iexact=slug)
        return render(request,self.template,context={self.model.__name__.lower():obj})      

       

    def post(self,request,slug):
        obj=self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.template_1))

