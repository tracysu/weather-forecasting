# https://open-meteo.com/
import requests

if __name__ == "__main__":
    lat = 40.7128
    longi = -74.0060
    # 1. figure out city from lat + longitude
    
    # access temperature, air quality, flood data for a given lat, longitude for past + upcoming week

    lat_long_url_search = (f'https://api.open-meteo.com/v1/dwd-icon?latitude={lat}&longitude={longi}&hourly=temperature_2m')
    
    city_url_search = f'https://geocoding-api.open-meteo.com/v1/search?name=New+York&count=10&language=en&format=json'
    
    response = requests.get(lat_long_url_search)
    result = response.json()
    times = result['hourly']['time']
    temps = result['hourly']['temperature_2m']
    print('times: ', len(times), 'temps: ', len(temps))