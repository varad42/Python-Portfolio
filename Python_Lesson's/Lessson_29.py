# Lesson 29: The API Project — live data, your code, something real 🛰️

# import requests
#
# city = input("City: ")
# geo = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=" + city)
# geo_data = geo.json()
# print(geo_data)
#
# print(geo_data["results"][0]["latitude"])

import requests

city = input("City: ")

# Call 1: city → coordinates
geo = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=" + city)
geo_data = geo.json()


if "results" not in geo_data:
    print("City not found")
else:

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # Call 2: coordinates → weather (the CHAIN — call 1's output feeds call 2's input!)
    weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current_weather=true")
    weather_data = weather.json()
    found_name = geo_data["results"][0]["name"]
    country = geo_data["results"][0]["country"]
    print(found_name + ", " + country + ": temperature: "  + str(weather_data["current_weather"]["temperature"]) + " windspeed: " + str(weather_data["current_weather"]["windspeed"]))

    print(weather_data)      # ← first run: STARE at the structure, like you just did