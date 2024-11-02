import requests

API_KEY = "c1024d4f098c1483b28503764858c9ec"
city = input("Enter a city name: ")

# Get latitude, longitude, and weather data in a single block
try:
    # Fetch geolocation data
    geocode_response = requests.get(
        "http://api.openweathermap.org/geo/1.0/direct",
        params={"q": city, "appid": API_KEY}
    )
    geocode_response.raise_for_status()  # Raise an error for bad responses
    geocode_data = geocode_response.json()[0]
    lat, lon = geocode_data['lat'], geocode_data['lon']

    # Fetch weather data
    weather_response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"lat": lat, "lon": lon, "appid": API_KEY}
    )
    weather_response.raise_for_status()
    weather_data = weather_response.json()
    
    # Display weather details
    weather = weather_data['weather'][0]['description']
    temperature = round(weather_data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
