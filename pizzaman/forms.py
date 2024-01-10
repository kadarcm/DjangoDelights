from django import forms
from .models import *

class ListInventoryF(forms.ModelForm):
    class Meta():
        model = Inventory
        fields =('__all__')