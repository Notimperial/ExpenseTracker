from django.contrib import admin
from django.urls import path
from Expense import views

app_name = 'Expense'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.Home, name='ExpenseView'),
    path('add/',views.ExpenseAddView, name='ExpenseAddView'),
    path('delete/<int:id>/',views.ExpenseDeleteView, name='ExpenseDeleteView'),
    path('edit/<int:id>/',views.ExpenseUpdateView, name='ExpenseUpdateView'),
    path('view/',views.ExpenseViewView, name='ExpenseViewView'),
]