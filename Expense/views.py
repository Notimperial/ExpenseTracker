from django.shortcuts import render
from django.http import HttpResponse
from django.forms import forms
from .forms import ExpenseForm

app_name = 'Expense'
# Create your views here.
def ExpenseView(request):
    return render(request, '/home/skyhill/Desktop/ExpenseTracker/expense_tracker/Expense/templates/view.html')

def ExpenseAddView(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Expense added successfully")
    else:
        form = ExpenseForm()

    return render(request, 'add.html', {'form': form})
    

def ExpenseDeleteView(request):
    return HttpResponse("This is the delete view with id ")

def ExpenseUpdateView(request):
    return HttpResponse("This is the update view with id ")