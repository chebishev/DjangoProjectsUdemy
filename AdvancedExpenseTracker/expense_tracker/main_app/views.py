from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense


def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    
    expenses = Expense.objects.all()
    expense_form = ExpenseForm()
    context = {
        'form': expense_form, 
        'expenses': expenses
        }
    return render(request, 'main_app/index.html', context)

def edit(request, id):
    current_expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=current_expense)
    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'main_app/edit.html', {'form': form})


def delete(request, id):
    if request.method == 'POST' and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    
    return redirect('index')