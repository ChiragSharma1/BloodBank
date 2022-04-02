from typing import Text
from django.forms import ModelForm, TextInput, NumberInput, Select
from .models import User


class DonarForm(ModelForm):
    class Meta:
        model = User
        # as user filling this form will be those who will be donating
        exclude = ['can_donate']
        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
                'style': 'max-width:300px;display:inline;'
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control',
                'style': 'max-width:300px;display:inline;'
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'style': 'max-width:100px;display:inline;'
            }),
            'gender': Select(attrs={
                'class': 'form-control',
                'style': 'max-width:200px;display:inline;margin-left:175px;',
            }),
            'blood_group': Select(attrs={
                'class': 'form-control',
                'style': 'max-width:100px;display:inline;margin-left:100px'
            }),
            'address': TextInput(attrs={
                'placeholder': 'Local Address',
                'class': 'form-control'
            }),
            'city': TextInput(attrs={
                'placeholder': 'City',
                'class': 'form-control',
                'style': 'max-width:300px;display:inline;'
            }),
            'state': TextInput(attrs={
                'placeholder': 'State',
                'class': 'form-control',
                'style': 'max-width:300px;display:inline;margin-left:120px;'
            }),
            'mobile': TextInput(attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control',
                'style': 'max-width:300px;display:inline;'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'style': 'max-width:300px;display:inline;margin-left:120px;'
            })

        }
