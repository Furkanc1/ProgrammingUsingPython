# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 01:04:46 2022

@author: john
"""

## now that you have a reliable way to get a lat and lon of a city, let's use it to get the weather for the city. 
## In part one of the assignment, you used the geocoding api to get the latitude and longitude of a city using its zipcode 
## copy your code from part one and now use the lat  / lon you returned to get the weather for the city

## Part 2 consists of using the current weather api
## Review the documentation of the Current Weather  API
##  https://openweathermap.org/current
## define a function to retrieve the current weather.
## Execute both the get_zip and getWeather functions to;
## print out the current city name, latitude, longitude, current weather description, current temperature, today's high and low


## Function definition
## 1. define a function called getWeather which
##  a. accepts two variables for latitude and longitude from the function you created in part 1
##  b. calls results module with the URL for weather API
##  c. returns current weather description, the current temperature, today's low and high temperatures
###
  

## Hint ###
## 1.  use the same API key you used for the get_zip function
## 2.  Follow the same steps to setup the function for weather as you did for the get_zip()
## 3.  Use the url for the current weather API found on the documentation page. 
## 4.  For the weather function in order to access the elements, look at the JSON returned. It is basically a dictionary of a set of dictionaries.
## 5.  For the temparatures, you can see in the JSON, it is part of the 'main: ' key. To access temp which is main:temp, simply assign 
##     a variable  to point the main key.  temperatures = myJSON['main'] 
##     then to get to the temperature number assign a second variable as such myTemp = temperatures['temp']
##     This allows us to go a level down in a dictionary
## 6.  For the current weather,  it is a dictionary inside a list
##     In order to access it, you will have to index it  with an offset.   weather = myJSON['weather'][0], which points to the 
##     description key. Then assign another varible to get to the value of description  weatherDESC = weather['desciption']
##     or you can assign a variable as in step 5 and include the index when accessing it. weatherDesc = weather[0]['desciption']
## 7.  Pretty Print the JSON out when writing the code, that will help you determine the key:value pair you will need. 

## Extra Credit:  use the status code returned from the weather api, to determine if a zip code is valid. An invalid zip code 
## will return a page not found code 400. 
## Extra Credit HINT - insert the test code into the get_zip() and based on the return code from the API, return values and test those values 
## in the main program.


""" Expected Output

with a valid zipcode:
    
Please enter a zipcode: 07430
The city name for 07430 is Mahwah
The latitude for 07430 is 41.0817
The longitude for 07430 is -74.1861
The current weather is overcast clouds
The current temperature is 65.1
Today's low 62.53 with a high of 68.74


with an invalid zip code for extra credit
    
Please enter a zipcode: 11111
The zipcode entered 11111 seems to be invalid.

"""
import requests

# prettify my return JSON
from pprint import pp 
apiKey = "d735ff976ff9608fe1853190a3b94c6f"
country = "US"

# def testing():
#     weatherData = f"https://api.openweathermap.org/data/2.5/weather?lat=40.748&lon=-73.9967&appid={apiKey}"
#     data = requests.get(weatherData)
#     forecastJson = data.json()

#     pp(forecastJson)
# testing()

# Converts temperatures from kelvin to Fahrenheit function:
def KelvToFahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# here we get the weather, we take in status, lat, lon, city, and zip as parameters to pass into variables
def getWeather(statusCode, lat, lon, city, zip, ):
    # where we get data from api
    weatherData = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"
    # .get() to get the long string of data
    statusCode = requests.get(weatherData)
    # jsonify the data we get back so its more readable
    forecastJson = statusCode.json()
    # pp(forecastJson)

    # variable for forecast (rain, snow, etc) reach into weather, and within weather, the description at index 0
    forecast = forecastJson['weather'][0]['description']
    # var for current temp (reach into main and get back temp)
    currTemp = forecastJson['main']['temp']
    # var for max temp, same process as current temp
    maxTemp = forecastJson['main']['temp_max']
    # var for min temp, same process as currTemp
    minTemp = forecastJson['main']['temp_min']

    # here we just pass in the value for the curr max and min temp, we convert it to be fahrenheit and round up 2 places
    currTempFahrenheit = round(KelvToFahrenheit(currTemp), 2)
    maxTempFahrenheit = round(KelvToFahrenheit(maxTemp), 2)
    minTempFahrenheit = round(KelvToFahrenheit(minTemp), 2)

    # here is what the user sees when program is finished running!
    print(f"\nThe call returned code: {statusCode} \n\nThe city name for {zip} is {city} \nThe latitude for {zip} is {lat} \nThe longitude for {zip} is {lon}\nThe Current Weather Forecast is: {forecast} with tempature of: {currTempFahrenheit} Fahrenheit\n\nHigh of the day: {maxTempFahrenheit} Fahrenheit\nLow of the day: {minTempFahrenheit} Fahrenheit")

# here is where we find the users location based on the inputted ZipCode Taking in (zip) as parameter
def findLocation(zip):
    # this is where we get back the lat and lon based on the zipcode
    latLonApiData = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip},{country}&appid={apiKey}"
    
    # here we get the data using requests.get()
    statusCode = requests.get(latLonApiData)

    # create a try except block in order to make sure that the users input (aka zip parameter) is a valid one and doesnt give back a keyError
    try:
        # create variables for lat lon city and json Object containing data
        myJSON = statusCode.json()
        lat = myJSON['lat']
        lon = myJSON['lon']
        city = myJSON['name']

        # finally send the variables we create as paraemters to the getWeather() function
        getWeather(statusCode, lat, lon, city, zip)
    except KeyError:
        # if there is a key error, the user will be notified it was not valid and will be sent back to askUSersInfo()
        print(f"The zipcode entered {zip} seems to be invalid, Try Again!")
        askUsersInfo()

# askUsersInfo is where we get the users input for their requested zipcode
def askUsersInfo():
    # here we TRY to get the users input, if they quit, we just send a goodbye message and kill program if not, we take their input and send it to the findLocation() function as a parameter
    try:
        usersChoice = input("Enter your zipcode EX: ##### or Quit (q) ").lower()
        if (usersChoice == "q"):
            print("goodbye!")
        else:
            findLocation(usersChoice)
    except ValueError:
        # else, if there is a value error (aka they put letters or symbols or anything they shouldnt) print out that it was not valid and send them back to the start of the function
        print(f"{usersChoice} was not valid, try again.")
        askUsersInfo()

# call the function for first time to initiate program when file is run!
askUsersInfo()