
from django import forms
import datetime

class MyForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )                                
    last_name = forms.CharField(
        label='Last Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    date_of_birth = forms.DateField(
        label='Date of Birth',
        initial=datetime.date.today,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    GenderChoices = [('M', 'Male'), ('F', 'Female')]
    gender = forms.ChoiceField(
        label='Gender',
        widget=forms.RadioSelect, 
        choices=GenderChoices
    )

# class PersonalForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(
#         max_length=3,
#         widget=forms.Select(choices=TITLE_CHOICES),
#     )
#     birth_date = forms.DateField(required=False)