from django.shortcuts import render
import http.client
import json
import datetime
from urllib.parse import quote



API_KEY="Enter You Api Key"

def convert_time_zone(timestamp, timezone_offset):
  dt = datetime.datetime.fromtimestamp(timestamp)
  dt_with_timezone = dt + datetime.timedelta(seconds=timezone_offset)
  return dt_with_timezone.strftime('%Y-%m-%d %H:%M:%S')


def index(request):
    weather_data= None
    if request.method == 'POST':
        city = request.POST.get('city')
       
        weather_data = get_weather(quote(city))
        

     
    return render(request, 'index.html',{'weather_data':weather_data})


def get_weather(city):
  conn = http.client.HTTPSConnection("api.openweathermap.org")
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
  conn.request("GET",url)

  response = conn.getresponse()
    
  if response.status == 200:
    data = json.loads(response.read())

    weather_data ={

        'city':city,
        'temperature':data['main']['temp'],
        'main_desc':data['weather'][0]['main'],
        'description':data['weather'][0]['description'],
        'lat':data['coord']['lat'],
        'lon':data['coord']['lon'],

        'icon_url': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",

        'feels_like':data['main']['feels_like'],
        'temp_min':data['main']['temp_min'],
        'temp_max':data['main']['temp_max'],
        'humidity':data['main']['humidity'],
        'pressure':data['main']['pressure'],
        'sea_level':data['main']['sea_level'],
        'grnd_level':data['main']['grnd_level'],


        'wind-s':data['wind']['speed'],
        'wind-d':data['wind']['deg'],
        
        'rain':data['rain']['1h'] if 'rain' in data else None,
        'snow':data['snow']['1h'] if 'snow' in data else None,
        'clouds':data['clouds']['all'],

        'visibility':data['visibility'],
        'sunrise': convert_time_zone(data['sys']['sunrise'],data['timezone']),
        'sunset':convert_time_zone(data['sys']['sunset'],data['timezone']),

        'timezone':convert_time_zone(data['dt'],data['timezone']),
        'date':convert_time_zone(data['dt'],data['timezone']),

        'id':data['id'],
        'name':data['name'],
        'cod':data['cod'],

        

    }

    return weather_data
  elif response.status == 404:
    return None
  else:
    return None



