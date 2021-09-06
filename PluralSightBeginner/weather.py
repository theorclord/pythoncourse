import requests

def getWeatherDescAndTemp():
    f = open("secrets.txt", "r")
    apiKey = f.read()
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey+"&units=metric"

    request = requests.get(url)
    json = request.json()
    description = json.get("weather")[0].get("description")
    tempMin = json.get("main").get("temp_min")
    tempMax = json.get("main").get("temp_max")
    return {"description": description, "tempMin": tempMin, "tempMax": tempMax}

# Print the results
weatherDict = getWeatherDescAndTemp()
print("Today's forecast is", weatherDict.get("description"))
print("The minimum temperature is", weatherDict.get("tempMin"))
print("The maximum temperature is", weatherDict.get("tempMax"))