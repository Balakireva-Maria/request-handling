from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import csv
CONTENT = []

from pagination.app.settings import BUS_STATION_CSV
with open(BUS_STATION_CSV, newline='', encoding='cp1251') as File:
    reader = csv.DictReader(File, delimiter = ',')
    for line in reader:
        CONTENT.append(line)
print(CONTENT)

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_number = int(request.GET.get('page',1))
    paginator = Paginator(CONTENT, 13)
    page_object = paginator.get_page(page_number)
    if page_object.has_next():
        next_page_url = reverse('bus_stations') + f'?page={page_object.next_page_number()}'
    else:
        next_page_url = None
    if page_number == 1:
        prev_page_url = None
    else:
        prev_page_url = page_object.previous_page_number()



    return render (request, 'index.html',  context={
        'bus_stations': (page_object.object_list),
        'current_page': page_object,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }
    )

