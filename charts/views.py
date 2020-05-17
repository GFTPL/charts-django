from django.shortcuts import render
from .models import City


def pie_chart(request):
    label =[]
    data = []


    querysets = City.objects.order_by('-population')
    for city in querysets:
        label.append(city.name)
        data.append(city.population)


    return render(request, 'home.html', {
        'label' : label,
        'data' : data,
    })

