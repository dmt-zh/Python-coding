import json
import requests

city = input('City? ')

api_url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': city,
    'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))
