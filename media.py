# -*- coding: utf-8 -*-
import urllib
import json
import omdbapikey
import os.path

class Movie():
    def __init__(self, movie_id, movie_trailer):
    #Get the data from OMDB, store the JSON object, close the connection
        movie_json = urllib.urlopen("http://www.omdbapi.com/?i="+movie_id)
        movie_data = json.load(movie_json)
        movie_json.close()
    #Check to see if we've got the image already
        if os.path.isfile("img/"+movie_id+".jpg"):
            self.movie_poster = "img/"+movie_id+".jpg"
        else:
            urllib.urlretrieve("http://img.omdbapi.com/?apikey="+omdbapikey.key()+"&i="+movie_id, "img/"+movie_id+".jpg")
            self.movie_poster = "img/"+movie_id+".jpg"
    #Store all the info from the JSON
    	self.movie_id = movie_id
    #    self.movie_poster  = movie_data["Poster"]
        self.movie_title = movie_data["Title"]
        self.movie_plot  = movie_data["Plot"]
        self.movie_year = movie_data["Year"]
        self.movie_genre = movie_data["Genre"]
        self.movie_imdbRating  = movie_data["imdbRating"]
        self.movie_imdbVotes  = movie_data["imdbVotes"]
        self.movie_rated = movie_data["Rated"]
        self.movie_metascore  = movie_data["Metascore"]
        self.movie_released = movie_data["Released"]
        self.movie_runtime = movie_data["Runtime"]
        self.movie_language  = movie_data["Language"]
        self.movie_country  = movie_data["Country"]
        self.movie_awards  = movie_data["Awards"]
        self.movie_director = movie_data["Director"]
        self.movie_writer = movie_data["Writer"]
        self.movie_actors  = movie_data["Actors"]
    #Apply the Youtube URL to the object
        self.movie_trailer = movie_trailer


