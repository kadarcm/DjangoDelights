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

class MenuListView(ListView):
    template_name= "pizzaman/menus.html"
    model= MenueItem

class CreateMenueView(CreateView):
    template_name ="pizzaman/general_form.html"
    model =MenueItem
    form_class = CreateMenueF
    success_url = reverse_lazy('menu_list')

class UpdateMenuView(UpdateView):
    template_name ="pizzaman/general_form.html"
    model =MenueItem
    form_class = UpdateMenuF
    success_url = reverse_lazy('menu_list')

def menu_recipe(request, menu_pk):
    context= {'recipe_itms': Recipe_list.objects.filter(entree=menu_pk).all()}
    context['inventory'] = list(Inventory.objects.all())
    context['form']= CreateRecipeItem()
    context['entree']=menu_pk
    if request.method == "POST":
        form = CreateRecipeItem(request.POST)
      
        if form.is_valid():
            new_item =Recipe_list()
            new_item.entree = MenueItem.objects.filter(entree= menu_pk).first()
            new_item.inventory=form.cleaned_data['inventory']
            new_item.recipe_amount_used=form.cleaned_data['recipe_amount_used']
            new_item.save()
        form.clean()
    
    return render(request, template_name='pizzaman\\recipe.html', context=context)

def sale_view(request):
    curent_sale = Sales.objects.filter(status='o').first()
    if not curent_sale  :
        curent_sale= Sales()
        curent_sale.save()
    context={'sales':curent_sale, "entrees":list(curent_sale.saleslines_set.all())}
    print(context)
    return render(request, template_name="pizzaman/sale.html", context=context)