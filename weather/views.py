import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


def convert_mps_to_kmph(mps):
    return round(mps * 3.6, 1)


# Create your views here.
def index(request):
    appid = ''
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    error = False

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            response = requests.get(url.format(city_name)).json()

            if 'main' in response:

                if not City.objects.filter(name=city_name).exists():
                    form.save()
                else:
                    form.add_error('name', 'City already exists.')

            else:
                form.add_error('name', 'Invalid city.')
                error = True

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    if error:
        error_message = 'Oops! Please write correct city name'
    else:
        error_message = None

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            wind_speed_mps = res['wind']['speed']
            wind_speed_kmph = convert_mps_to_kmph(wind_speed_mps)

            city_info = {
                'city': city.name,
                'temp': round(res['main']['temp']),
                'icon': res['weather'][0]['icon'],
                'pressure': res['main']['pressure'],
                'humidity': res['main']['humidity'],
                'wind_speed': wind_speed_kmph,
                'error': False,
                'obj': city
            }
            if not form.errors.get('name'):
                all_cities.append(city_info)

    reversed_city = reversed(all_cities)

    context = {'all_info': reversed_city, 'form': form, 'error_message': error_message}

    return render(request, 'weather/index.html', context)


def main_page(request):
    return render(request, 'weather/main.html')


def delete(request, city_id):
    delete_city = get_object_or_404(City, id=city_id)
    delete_city.delete()
    return redirect('home')
