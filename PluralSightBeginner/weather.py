import requests
f = open("secrets.txt", "r")

apiKey = f.read()
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey

request = requests.get(url)
json = request.json()

print(json)