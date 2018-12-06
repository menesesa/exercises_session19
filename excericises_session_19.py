#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 01:30:40 2018

@author: alemeneses
"""
#%%
# Create a function that uses the requests library to get the lyrics of a song.

# You can use the lyrics.ovh api as described here: 
# https://lyricsovh.docs.apiary.io/#reference/0/lyrics-of-a-song/search?console=1

import requests
def get_lyrics(artist, song_name):
    #url = "https://api.lyrics.ovh/v1/" + artist + "/" + song_name
    url = "https://api.lyrics.ovh/v1/{}/{}".format(artist, song_name)
    
    response = requests.get(url)

    print(response.json()["lyrics"])

#%%

#Create a function that returns the current latitude and longitude of the ISS

#http://api.open-notify.org/

def iss_location(): 
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url)
    
    position = response.json()["iss_position"]
    
    print ("currently the ISS is in {}:{}".format(position["latitude"], position["longitude"]))
    

      
    print("https://www.google.com/maps/search/{}".format(position["latitude"] + "," + position["longitude"])) 
    

#%%

# using the given population API, create a program that:

# - gets a list of all available countries
# - Gets the first 10 countries
# - Gets the country's today & tomorrow population.
# http://api.population.io/#!/countries/listCountries 
    
def countries_population(): 
    
    url = "http://api.population.io:80/1.0/countries"
    
    response = requests.get(url)
    
    countries = []
    
    for country in set(response.json()["countries"]):
        
        if country.upper() == country: 
            continue
  
        else: 
            if len(countries) < 10: 
                countries.append(country)
                
    for country in countries: 
        url = "http://api.population.io:80/1.0/population/" + country + "/today-and-tomorrow/"
        response = requests.get(url)
        
        population = response.json()["total_population"]
       
        print(country) 
       
        for day in population: 
           print(day["date"] + ": " + str(day["population"]))
       

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    