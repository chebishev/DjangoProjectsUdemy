from django.shortcuts import render
from .forms import ExpenseForm
# Create your views here.
def index(request):
    form = ExpenseForm()
    return render(request, 'main_app/index.html', {'form': form})