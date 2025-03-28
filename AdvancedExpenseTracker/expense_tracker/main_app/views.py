from django.shortcuts import render
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