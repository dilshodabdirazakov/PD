from django.shortcuts import render
from django.http import HttpResponse
from .models import Load

# Create your views here.

def index(request):
    loads = Load.objects.all()
    return render(request, "home.html", {'loads': loads})
    