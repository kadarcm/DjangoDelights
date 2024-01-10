from django import forms
from .models import *

class CretateInventoryF(forms.ModelForm):
    class Meta():
        model = Inventory
        fields =('__all__')

class UpdateInventoryF(forms.ModelForm):
    class Meta():
        model = Inventory
        fields =['amount_on_hand','cost_uom']