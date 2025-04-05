from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.forms import forms
from .forms import ExpenseForm
from .models import Expense

app_name = 'Expense'
# Create your views here.
def Home(request):
    return render(request, '/home/skyhill/Desktop/ExpenseTracker/expense_tracker/Expense/templates/home.html')


def ExpenseAddView(request):
    success_message = "None"
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Expense added successfully!"
    else:
        form = ExpenseForm()

    return render(request, 'add.html', {'form': form, 'success_message': success_message})
    

def ExpenseDeleteView(request, id):
    expense = get_object_or_404(Expense, pk=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('Expense:ExpenseViewView')  
    return render(request, 'delete.html', {'expense': expense})

def ExpenseUpdateView(request, id):
    expense = get_object_or_404(Expense, pk=id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('Expense:ExpenseViewView')  # Make sure this URL name exists
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'update.html', {'form': form, 'expense': expense})

     
    
def ExpenseViewView(request):
    expense_view = Expense.objects.all()
    return render(request, 'view.html', {'expense_view': expense_view})


