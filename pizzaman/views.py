from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'pizzaman\\home.html')

def about(request):
    return render(request, 'pizzaman\\about.html')

class InventoryListView(ListView):
    template_name= "pizzaman/inventory.html"
    model= Inventory

class CreateIventoryView(CreateView):
    template_name ="pizzaman/general_form.html"
    model =Inventory
    form_class = CretateInventoryF
    success_url = reverse_lazy('inv_list')

class UpdateIventoryView(UpdateView):
    template_name ="pizzaman/general_form.html"
    model =Inventory
    form_class = UpdateInventoryF
    success_url = reverse_lazy('inv_list')