from django import forms
from .models import *

class Supplier(forms.ModelForm):
    class Meta:
        model = supplier
        fields = ['name', 'number', 'address', 'account_Number']

class Spareparts(forms.ModelForm):
    class Meta:
        model = sparepart
        fields = ['id_code', 'type', 'model', 'quantity', 'Price_Per_Unit', 'Price_Per_Unit_Imp']

