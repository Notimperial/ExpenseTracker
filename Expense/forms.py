from django import forms
from Expense.models import Expense  

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'description']


    