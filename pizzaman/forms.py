from django import forms
from .models import *

class CretateInventoryF(forms.ModelForm):
    title= "Add Inventory Item"
    class Meta():
        model = Inventory
        fields =('__all__')

class UpdateInventoryF(forms.ModelForm):
    title="Inventory Count Update"
    class Meta():
        model = Inventory
        fields =['amount_on_hand','cost_uom']