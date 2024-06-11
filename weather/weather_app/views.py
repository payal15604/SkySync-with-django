import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=0ade168c39f8c62d4ac1bf53e01bb378"
    cities = City.objects.all()
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities: 

        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'city': city.name,
            'temperature': round(r['main']['temp'] - 273.15, 2),
            'weather': r['weather'][0]['main'],
            'humidity': r['main']['humidity'],
            'wind_speed': r['wind']['speed'],
            'visibility': r['visibility'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    #print(weather_data)

    context = {'data_cities' : weather_data, 'form': form}

    return render(request,'index.html', context)
    