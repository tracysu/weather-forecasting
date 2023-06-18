# https://open-meteo.com/
import requests

if __name__ == "__main__":
    lat = 40.7128
    longi = -74.0060
    # 1. figure out city from lat + longitude
    
    # access temperature, air quality, flood data for a given lat, longitude for past + upcoming week

    lat_long_url_search = (f'https://api.open-meteo.com/v1/dwd-icon?latitude={lat}&longitude={longi}&hourly=temperature_2m')
    
    city_url_search = (f'https://geocoding-api.open-meteo.com/v1/search?name=New+York&count=10&language=en&format=json')
    
    weather_interpretation = {
    "00": "Clear sky",
    "01": "Scattered clouds",
    "02": "Partly cloudy",
    "03": "Cloudy sky",
    "04": "Smoke/ash",
    "05": "Haze",
    "06": "Dust, no wind",
    "07": "Dusty wind",
    "08": "Dusty whirlwinds",
    "09": "Rain showers",
    "10": "Mist",
    "11": "Intermittent shallow fog",
    "12": "Shallow fog",
    "13": "Lightning, no storm",
    "14": "Very light rain",
    "15": "Distant rain",
    "16": "Incoming rain",
    "17": "Incoming thunderstorm",
    "18": "Small thunderstorm",
    "19": "Funnel clouds or tornado",
    "20": "Light drizzle",
    "21": "Rain",
    "22": "Snow",
    "23": "Rain and snow",
    "24": "Freezing drizzle",
    "25": "Rain showers",
    "26": "Snow showers",
    "27": "Hail showers",
    "28": "Cold fog",
    "29": "Thunder",
    "30": "Decreasing duststorm",
    "31": "Duststorm",
    "32": "Worsening duststorm",
    "33": "Severe decreaing duststorm",
    "34": "Severe duststorm",
    "35": "Severe worsening duststorm",
    "36": "Light blowing snow",
    "37": "Blowing snow",
    "38": "Drifting snow",
    "39": "Heavy drifting snow",
    "40": "Distant fog",
    "41": "Patches of fog",
    "42": "Thinning fog, sky visible",
    "43": "Thinning fog, sky not visible",
    "44": "Fog, sky visible",
    "45": "Fog, sky not visible",
    "46": "Worsening fog, sky visible",
    "47": "Worsening fog, sky not visible",
    "48": "Fog and frost, sky visible",
    "49": "Fog and frost, sky not visible",
    "50": "Intermittent light drizzle",
    "51": "LIght drizzle",
    "52": "Intermittent moderate drizzle",
    "53": "Moderate drizzle",
    "54": "Intermittent heavy drizzle",
    "55": "Heavy drizzle",
    "56": "Light freezing drizzle",
    "57": "Heavy freezing drizzle",
    "58": "Light drizzle and rain",
    "59": "Heavy drizzle and rain",
    "60": "Intermittent light rain",
    "61": "Light rain",
    "62": "Intermittent heavy rain",
    "63": "Moderate rain",
    "64": "Intermittent heavy rain",
    "65": "Heavy rain",
    "66": "Light freezing rain",
    "67": "Heavy freezing rain",
    "68": "Light rain and snow",
    "69": "Heavy rain and snow",
    "70": "Intermittent light snow",
    "71": "Light snow",
    "72": "Intermittent moderate snow",
    "73": "Moderate snow",
    "74": "Intermittent heavy snow",
    "75": "Heavy snow",
    "76": "Diamond Dust",
    "77": "Snow grains",
    "78": "Snow crystals",
    "79": "Ice Pellets",
    "80": "Slight rain showers",
    "81": "Heavy rain showers",
    "82": "Violent rain shower",
    "83": "Slight rain/snow showers",
    "84": "Heavy rain/snow showers",
    "85": "Slight snow showers",
    "86": "Heavy snow showers",
    "87": "Slight snow pellet showers",
    "88": "Heavy snow pellet showers",
    "89": "Light hail showers",
    "90": "Heavy Hail showers",
    "91": "Slight rain",
    "92": "Heavy rain",
    "93": "Slight snow",
    "94": "Heavy snow and hail",
    "95": "Thunderstorm",
    "96": "Thunderstorm with hail",
    "97": "Thunderstorm + rail/snow",
    "98": "Thunderstorm + duststorm",
    "99": "Thunderstorm with heavy hail",
    # Add more codes and descriptions as needed
}



    
    response = requests.get(lat_long_url_search)
    result = response.json()
    times = result['hourly']['time']
    temps = result['hourly']['temperature_2m']
    print('times: ', len(times), 'temps: ', len(temps))