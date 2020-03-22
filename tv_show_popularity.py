# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:15:41 2020

@author: Hp
"""


import requests
import pandas as pd
from bs4 import BeautifulSoup
import pickle


url = "http://www.imdb.com/chart/toptv/"
r = requests.get(url)
html = r.text
html[0:200]

# Use Beautiful soup to extract the imdb numbers from the webpage
soup = BeautifulSoup(html, "lxml")

#soup = BeautifulSoup(r.content, features=“html”)

# Scrape the IMDb numbers for the 250 top rated shows

show_list = []
for tbody in soup.findAll('tbody', class_='lister-list'):
    for title in tbody.findAll('td', class_='titleColumn'):
        show_list.append(str(title.findAll('a')).split("/")[2])

print(show_list)





DO_NOT_RUN = True     # Do not run when notebook is loaded to avoid unnecessary calls to the API

if not DO_NOT_RUN:
    shows = pd.DataFrame()
    for show_id in show_list:
            try:
                print (show_id)
                # Get the tv show info from the api
                url = "http://api.tvmaze.com/lookup/shows?imdb=" + show_id
                r = requests.get(url)

                # convert the return data to a dictionary
                json_data = r.json()

                # load a temp datafram with the dictionary, then append to the composite dataframe
                temp_df = pd.DataFrame.from_dict(json_data, orient='index', dtype=None)
                ttemp_df = temp_df.T     # Was not able to load json in column orientation, so must transpose
                shows = shows.append(ttemp_df, ignore_index=True)
            except: 
                print (show_id)# " could not be retrieved from api"

    shows.head()