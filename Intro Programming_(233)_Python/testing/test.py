#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:20:24 2024

@author: stevedavis
"""

import requests
from PIL import Image
from io import BytesIO
import random

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": "e0d69ed175msh01003773d992fc2p10992fjsnfa7def0b9f4c",
    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
movies_data = response.json()


#print out list of all 100 movies on this api
count = 1
for movie in movies_data:
    print(f"{count}. {movie['title']}")
    count += 1
print("Here are the titles for all 100 movies in IMDB Top 100")


def get_movie_info(movie_title):
    for movie in movies_data:
        if movie['title'].lower() == movie_title.lower():
            return movie
    return None


def random_movie():
    randnum = random.randint(0, 99)
    return movies_data[randnum]


# Function to ask the user if they want a random movie
def ask_random_movie():
    random_movie_info = random_movie()
    print("\nRandom Movie:")
    print("Title:", random_movie_info['title'])
    print("Year:", random_movie_info['year'])
    if 'rating' in random_movie_info:
        print("Rating:", random_movie_info['rating'])
    else:
        print("Rating: N/A")
    print("Description:", random_movie_info['description'])
        
    # Join genre strings into a single string separated by commas
    if 'genre' in random_movie_info:
        genre = ', '.join(random_movie_info['genre'])
        print("Genre:", genre)
    else:
        print("Genre: N/A")
        
    # Display image if available
    if 'image' in random_movie_info:
        image_url = random_movie_info['image']
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        image.show()
    else:
        print("Image not available.")


def user_movie(movie_title):
    movie_info = get_movie_info(movie_title)
    if movie_info:
        print ("\n")
        print("Title:", movie_info['title'])
        print("Year:", movie_info['year'])
        if 'rating' in movie_info:
            print("Rating:", movie_info['rating'])
        else:
            print("Rating: N/A")
        print("Description:", movie_info['description'])
        
        # Join genre strings into a single string separated by commas
        if 'genre' in movie_info:
            genre = ', '.join(movie_info['genre'])
            print("Genre:", genre)
        else:
            print("Genre: N/A")
        
        # Display image if available
        if 'image' in movie_info:
            image_url = movie_info['image']
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            image.show()
        else:
            print("Image not available.")
    else:
        print("Movie not found.")


# main
is_running = True

while is_running:
    print ("\n")
    user_input = input("Enter the title of the movie, type 'random' for a random movie, or 'quit' to exit: ")
    if user_input.lower() == 'quit':
        print ("Bye!!!")
        is_running = False
    elif user_input.lower() == 'random':
        ask_random_movie()
    else:
        user_movie(user_input)