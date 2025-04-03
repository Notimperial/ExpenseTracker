from django.contrib import admin
from django.urls import path
from Expense import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.ExpenseView, name='ExpenseView'),
    path('add/',views.ExpenseAddView, name='ExpenseAddView'),
    path('delete/',views.ExpenseDeleteView, name='ExpenseDeleteView'),
    path('update/',views.ExpenseUpdateView, name='ExpenseUpdateView'),
]