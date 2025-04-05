from django import forms
from Expense.models import Expense  

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'styled-input'}),
            'amount': forms.NumberInput(attrs={'class': 'styled-input'}),
            'description':forms.Textarea(attrs = {"class": 'styled-input'}),
        }
       