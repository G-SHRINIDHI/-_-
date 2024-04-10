import tkinter as tk
import requests

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    # Extracting relevant weather information
    if weather_data['cod'] == 200:  # Check if the request was successful
        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        weather_info_label.config(text=f'{city_name}\nTemperature: {temperature}°C\nDescription: {description}')
    else:
        weather_info_label.config(text='City not found!')

# Tkinter setup
root = tk.Tk()
root.title('Weather App')

# Input field for city
city_label = tk.Label(root, text='Enter City:')
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Button to fetch weather
get_weather_button = tk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.pack()

# Label to display weather information
weather_info_label = tk.Label(root, text='')
weather_info_label.pack()

root.mainloop()
