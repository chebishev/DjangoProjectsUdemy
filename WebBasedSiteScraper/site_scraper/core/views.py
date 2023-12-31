from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link
from .forms import SearchForm
# Create your views here.


def scrape(request):
    form = SearchForm(request.POST or None)
    if request.method == "POST":
        site = request.POST.get('site', '')

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'core/result.html', {'data': data, 'form': form})


def delete(request):
    Link.objects.all().delete()
    return redirect('/')
