
from django import forms

class MyForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control"})\
    )                                
    last_name = forms.CharField(
        label='Last Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )