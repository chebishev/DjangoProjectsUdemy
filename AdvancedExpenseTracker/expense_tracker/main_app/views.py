from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
import datetime
from django.db.models import Sum

def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    # Get all expenses
    all_expenses = Expense.objects.all()
    total_expenses = all_expenses.aggregate(Sum('amount'))

    last_year = datetime.date.today() - datetime.timedelta(days=365)
    year_data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = year_data.aggregate(Sum('amount'))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    month_data = Expense.objects.filter(date__gt=last_year)
    monthly_sum = month_data.aggregate(Sum('amount'))

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    week_data = Expense.objects.filter(date__gt=last_year)
    weekly_sum = week_data.aggregate(Sum('amount'))


    expense_form = ExpenseForm()
    context = {
        'form': expense_form, 
        'all_expenses': all_expenses,
        'total_expenses': total_expenses, 
        'yearly_sum': yearly_sum,
        'monthly_sum': monthly_sum,
        'weekly_sum': weekly_sum
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