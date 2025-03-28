from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense


def index(request):
        expenses = Expense.objects.all()
        if request.method == 'POST':
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
        
        form = ExpenseForm()
        context = {
            'form': form, 
            'expenses': expenses
            }
        return render(request, 'main_app/index.html', context)

def edit(request, id):
    current_expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=current_expense)
    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=current_expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'main_app/edit.html', {'form': form})