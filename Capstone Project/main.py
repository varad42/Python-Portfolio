from storage_1 import load_profile, save_profile, load_tasks
from todo_app import run, show_quote
import requests
from datetime import date

profile = load_profile()


def show_temperature(city):
    try:
        geo = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=" + city)
        geo_data = geo.json()

        if "results" not in geo_data:
            print("City not found")
        else:

            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]

            # Call 2: coordinates → weather (the CHAIN — call 1's output feeds call 2's input!)
            weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(
                lon) + "&current_weather=true")
            weather_data = weather.json()
            found_name = geo_data["results"][0]["name"]
            country = geo_data["results"][0]["country"]
            print(found_name + ", " + country + ": temperature: " + str(
                weather_data["current_weather"]["temperature"]) + " windspeed: " + str(
                weather_data["current_weather"]["windspeed"]))
    except requests.exceptions.ConnectionError:
        print("Weather unavailable (no internet connection).")




def show_tasks():
    todos = load_tasks()
    for item in todos:
        print(item.display())
def greet(name):
    print("Hello " + name + " Welcome ")


# ---------- FIRST-RUN SETUP (setup only, nothing else!) ----------
if profile is None:
    print("First time setup")
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    profile = {"name": name, "city": city}
    save_profile(profile)
    print("Profile created successfully!")

# ---------- THE BRIEFING (one copy, everyone passes through) ----------
greet(profile["name"])
print("Today's Date: " + str(date.today()))
show_tasks()
show_temperature(profile["city"])

manage_tasks = input("Manage tasks? (yes/no): ")
if manage_tasks == "yes":
    run()

show_quote()






