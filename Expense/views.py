from django.shortcuts import render
from django.http import HttpResponse

app_name = 'Expense'
# Create your views here.
def ExpenseView(request):
    return render(request, '/home/skyhill/Desktop/ExpenseTracker/expense_tracker/Expense/templates/view.html')