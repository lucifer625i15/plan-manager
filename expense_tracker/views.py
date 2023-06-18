from django.forms import ValidationError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from expense_tracker.models import Expense

def expense_list(request):

    expenses = Expense.objects.filter(user= request.user)

    return render(request, 'expence_list.html', {'expenses':expenses})

def expense_add(request):

    if request.method == 'POST':
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        date = request.POST.get('date')

        if Expense.objects.filter(category=category).exists():
            return HttpResponse("Category already exists")
        try:
            expense = Expense.objects.create(user=request.user, amount=amount, category=category, date=date)
            expense.save()
        
        except ValidationError as e:
            return HttpResponse(str(e))
    return render(request, 'add_expense.html')
        
def expense_update(request, id):

    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        
        amount = request.POST('amount')
        date = request.POST('date')
        expense.amount =amount
        expense.date =date
        expense.save()
        return redirect('expense_list')
    
    return render(request, 'expense_update.html')

def expense_delete(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_delete.html')
