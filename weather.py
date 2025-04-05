import tkinter as tk
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text=f"City not found: {city}")
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"Weather in {city}:\n"
            f"{weather.capitalize()}, {temp}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )

        result_label.config(text=result)

    except Exception as e:
        result_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Simple Weather App")
root.geometry("350x300")  

tk.Label(root, text="Enter City Name:").pack(pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    wraplength=320,
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()
