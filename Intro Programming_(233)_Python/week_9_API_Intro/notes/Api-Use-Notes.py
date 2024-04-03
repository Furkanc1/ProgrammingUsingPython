# Testing JSON Endpoints

import requests

# used to show api that you are not malicious when accessing data
headers = {
    "Content-Type":"application/json", 
    "User-agent":"Mozilla",
}

# get method for getting data from api (stored in "results" variable created by YOU (me) )
results = requests.get('http://api.open-notify.org/astros.json', headers=headers)

#printing the status (200)
print(results.status_code) 

# put the returned Data as a JSON object in a variable
myJSON  = results.json()

# print the Json Data (in JSON format) (aka object format)
print(myJSON)

# specifically looking into the data and grabbing what you need (in this case "message")
# which will return 'success'
print (myJSON['message'])

# returns first person (everything in their object aka: {'name': '___' + 'craft': '____')
print (myJSON['people'][0])

# returns first persons name (name specifically)
print (myJSON['people'][0]['name'])

# will print out all the names in people object (dictionary) from api
for people in myJSON['people']:
    print(people['name'])


# Using P-Print: (same code, just with PP (pretty-print) being used)
    
# from pprint import pp # prettify my return JSON

# results = requests.get('http://api.open-notify.org/astros.json')

# myJSON  = results.json()

# print (myJSON['message'])

# print(myJSON)

# pp(myJSON)

# WEATHER_API_TEMPLATE:
import requests

apiKey = "enter key here"
countryCode = 'US'
zipCode = '07430'
lat = ""
lon = ""
apiUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"

