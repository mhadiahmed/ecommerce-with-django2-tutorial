from django import forms
from .models import order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ('first_name','last_name','email','address','postal_code','city',)
    