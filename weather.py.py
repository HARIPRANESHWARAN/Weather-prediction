import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")
    else:
        print("Error fetching weather data. Check the city name or your API key.")

# Replace with your city and OpenWeatherMap API key
city_name = input("Enter city name: ")
api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
get_weather(city_name, api_key)
