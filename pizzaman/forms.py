from django import forms
from .models import *

class CretateInventoryF(forms.ModelForm):
    title= "Add Inventory Item"
    class Meta():
        model = Inventory
        fields ='__all__'

class UpdateInventoryF(forms.ModelForm):
    title="Inventory Count Update"
    class Meta():
        model = Inventory
        fields =['amount_on_hand','cost_uom']

class CreateMenueF(forms.ModelForm):
    title=""
    class Meta():
        model = MenueItem
        fields= "__all__"


class UpdateMenuF(forms.ModelForm):
    title=""
    class Meta():
        model = MenueItem
        fields =['price']

class CreateRecipeItemF(forms.ModelForm):
    title=""
    class Meta():
        model =Recipe_list
        fields =['inventory', 'recipe_amount_used']

class CreateSaleItemF(forms.Form):
    trans_id= forms.IntegerField()
    entree =forms.CharField(max_length=50)
    qty=forms.IntegerField()

    
    