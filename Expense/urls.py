from django.contrib import admin
from django.urls import path
from Expense import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.ExpenseView, name='ExpenseView'),
]