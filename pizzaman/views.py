
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'pizzaman/home.html')

def about(request):
    return render(request, 'pizzaman/about.html')

class InventoryListView(ListView):
    template_name= "pizzaman/inventory.html"
    model= Inventory

class CreateIventoryView(LoginRequiredMixin, CreateView):
    template_name ="pizzaman/general_form.html"
    model =Inventory
    form_class = CretateInventoryF
    success_url = reverse_lazy('inv_list')

class UpdateIventoryView(LoginRequiredMixin, UpdateView):
    template_name ="pizzaman/general_form.html"
    model =Inventory
    form_class = UpdateInventoryF
    success_url = reverse_lazy('inv_list')

class MenuListView(ListView):
    template_name= "pizzaman/menus.html"
    model= MenueItem

class CreateMenueView(LoginRequiredMixin, CreateView):
    template_name ="pizzaman/general_form.html"
    model =MenueItem
    form_class = CreateMenueF
    success_url = reverse_lazy('menu_list')

class UpdateMenuView(LoginRequiredMixin, UpdateView):
    template_name ="pizzaman/general_form.html"
    model =MenueItem
    form_class = UpdateMenuF
    success_url = reverse_lazy('menu_list')

@login_required()
def menu_recipe(request, menu_pk):
    context= {'recipe_itms': Recipe_list.objects.filter(entree=menu_pk).all()}
    context['inventory'] = list(Inventory.objects.all())
    context['form']= CreateRecipeItemF()
    context['entree']=menu_pk
    if request.method == "POST":
        form = CreateRecipeItemF(request.POST)
      
        if form.is_valid():
            new_item =Recipe_list()
            new_item.entree = MenueItem.objects.filter(entree= menu_pk).first()
            new_item.inventory=form.cleaned_data['inventory']
            new_item.recipe_amount_used=form.cleaned_data['recipe_amount_used']
            new_item.save()
        form.clean()
    
    return render(request, template_name='pizzaman/recipe.html', context=context)

@login_required()
def sale_view(request):
    curent_sale = Sales.objects.filter(status='o').first()
    if not curent_sale  :
        curent_sale= Sales()
        curent_sale.save()
    menu=list(MenueItem.objects.all())
    context={'sales':curent_sale, "entrees":list(curent_sale.saleslines_set.all()), 'menu':menu}
    return render(request, template_name="pizzaman/sale.html", context=context)

@login_required()
def sale_add_item(request):
    if request.method == 'POST':
        form = CreateSaleItemF(request.POST)
        if form.is_valid():
            new_item=SalesLines()
            new_item.transaction_id= Sales.objects.filter(transaction_id = form.cleaned_data['trans_id']).first()
            new_item.entree = MenueItem.objects.filter(entree= form.cleaned_data['entree']).first()
            new_item.qty = form.cleaned_data['qty']
            new_item.save()
    return redirect('sale_add')

@login_required()
def sale_remove_item(request, pk):
    print(pk)
    SalesLines.objects.filter(line_id=pk).first().delete()
    return redirect('sale_add')

@login_required()
def cancel_sale(request, pk):
    Sales.objects.filter( transaction_id =pk).first().delete()
    return redirect('home')

@login_required()
def complete_sale(request, pk):
    current_sale=Sales.objects.filter( transaction_id =pk).first()
    current_sale.status='c'
    current_sale.total_amount=current_sale.calculate_sale_total()
    if current_sale.total_amount ==0:
        return redirect('home')
    current_sale.save()
    current_sale.line_item_consume()

    return redirect('home')

def todays_sales(request):
    sales=list(Sales.objects.filter(created_dt__gt= timezone.datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)).all())
    context={'sales':sales}
      
    return render(request=request, template_name='pizzaman/today_sales.html', context=context)
