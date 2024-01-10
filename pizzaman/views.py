from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic import ListView
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'pizzaman\\home.html')

def about(request):
    return render(request, 'pizzaman\\about.html')

class InventoryListView(ListView):
    template_name= "pizzaman/inventory.html"
    model= Inventory