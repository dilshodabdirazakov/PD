from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Load
from .forms import LoadForm

# Create your views here.



def index(request):
    
    loads = Load.objects.all()
    context =  {'loads': loads}
    return render(request, "base.html", context)
    