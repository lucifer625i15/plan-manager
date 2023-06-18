from django.urls import path
from . import views
urlpatterns = [
    path('', views.expense_list, name="expense_list"),
    path('add-expense/', views.expense_add, name=" expense_add"),
    path('update-expense/<int:id>', views.expense_update, name="expense_update"),
    path('delete-expense/<int:id>', views.expense_delete, name="expense_delete"),
]