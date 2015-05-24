# -*- coding: utf-8 -*-
import media
import trailer_park

#For each movie, pass its IMDb ID and Youtube trailer ID

movies = [
	media.Movie("tt0443455","uNrgu8DO7-w"), #Brand upon the brain
	media.Movie("tt1182345","E-E13MP3o54"), #Moon
	media.Movie("tt0076759","1g3_CFmnU7k"), #Star Wars
	media.Movie("tt0050086","AyDdnqYxhd8"), #3:10 to Yuma
	media.Movie("tt0105695","XDAXGILEdro"), #Unforgiven
	media.Movie("tt0335266","sU0oZsqeG_s"), #Lost in Translation
	media.Movie("tt0780504","CWX34ShfcsE"), #Drive
	media.Movie("tt0087469","HOwWfns4qqw"), #Indiana Jones and the Temple of Doom
	media.Movie("tt0056443","ZHIRcbAMFHo"), #Sanjuro
	media.Movie("tt0091042","R-P6p86px6U"), #Ferris Bueller's Day Off
	media.Movie("tt0910936","_GnV2u30oOU"), #Pineapple Express
	media.Movie("tt0262432","shVmpGH-YxA"), #George Washington
	media.Movie("tt0074174","sF6De-XP7x4"), #Bad News Bears
	media.Movie("tt0356721","2eOLOmCjRPY"), #I Heart Huckabees
	media.Movie("tt0365748","yfDUv3ZjH2k"), #Shaun of the Dead
	media.Movie("tt0393109","uM7E0XGiyrc"), #Brick
	media.Movie("tt0206634","Q9CFcTY_pik"), #Children of Men
	media.Movie("tt0416320","wISRAOb6xm0"), #Match Point
	media.Movie("tt0243759","rikiGMGhKVw"), #The American Astronaut
	media.Movie("tt0050613","PoYzsDVyFRU"), #Throne of Blood
	media.Movie("tt0061747","0Eh-FOdu5ho"), #Hang 'em High
	media.Movie("tt0119107","jPbdwsZh38o"), #Fast, Cheap & Out of Control
	media.Movie("tt0070334","GeNyD9UFXHs"), #The Long Goodbye
	media.Movie("tt0056869","LrN_U830_Gc"), #The Birds
	media.Movie("tt0443680","-FsN_utDELE"), #The Assassination of Jesse James by the Coward Robert Ford
	media.Movie("tt0118799","16RZHqCIy9M"), #Life is Beautiful
	media.Movie("tt0379217","P_7uQsP2TBk"), #Coffee and Cigarettes
	media.Movie("tt0038355","VjJlBnfyiI4"), #The Big Sleep
	media.Movie("tt0091167","Qtgw38Yq2Qs"), #Hannah and Her Sisters
	media.Movie("tt0103905","bcPhaieTg4o"), #Man Bites Dog
	media.Movie("tt0266697","ot6C1ZKyiME"), #Kill Bill
	media.Movie("tt0079470","tOOVm4kY4lE"), #Life of Brian
	media.Movie("tt0068646","sY1S34973zA"), #The Godfather
	media.Movie("tt0047478","MwvpUtc1hBU"), #Seven Samurai
	media.Movie("tt0057012","1gXY3kuDvSU"), #Dr. Strangelove
	media.Movie("tt0071315","3aifeXlnoqY"), #Chinatown
]

trailer_park.open_movies_page(movies)