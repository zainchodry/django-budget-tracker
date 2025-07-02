from django import forms
from . models import *
from django.contrib.auth.forms import UserChangeForm


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['id', 'title', 'amount', 'category', 'type', 'date']

        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'amount':forms.NumberInput(attrs = {'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'type':forms.Select(attrs = {'class':'form-control'}),
            'date' : forms.DateInput(attrs = {'type':'date', 'class':'form-control'})
        }
        lebels = {
            'title':'Title',
            'amount':'Amount',
            'category':'Category',
            'type':'Type',
            'date':'Date'
        }

