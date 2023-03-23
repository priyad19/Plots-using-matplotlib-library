from django import forms
from .models import Addresses

class DateForm(forms.Form):
    villages = Addresses.objects.values_list('village', flat=True).distinct()
    village = forms.ChoiceField(choices=[(v, v) for v in villages],label='Village')
