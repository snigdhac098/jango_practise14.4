from django.shortcuts import render
from . forms import PractiseForm
from . import models
# Create your views here.

def django_form(request):
    if request.method == "POST":
         form=PractiseForm(request.POST)
         if form.is_valid():
           print(form.cleaned_data)
           
    else:
        form=PractiseForm()
    return render(request,'home.html',{'form':form})



def viewmodel(request):
    view=models.PractiseModel.objects.all()
    return render(request,"index.html",{'data' : view})


