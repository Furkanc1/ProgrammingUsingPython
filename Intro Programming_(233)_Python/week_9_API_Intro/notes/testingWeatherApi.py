# # WEATHER_API_TEMPLATE:
# import requests

# apiKey = "enter key here"
# countryCode = 'US'
# zipCode = '07430'
# lat = ""s
# lon = ""
# apiUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"

import requests

api_key = "ENTER KEY HERE"

headers = {"Content-Type":"application/json", "User-agent":"Mozilla"}

country_code='US'
myZip = '07430'
myURL = f"http://api.openweathermap.org/geo/1.0/zip?zip={myZip},{country_code}&appid={api_key}"

results=requests.get(myURL,headers=headers)

print(results.status_code)