# -*- coding: utf-8 -*-
import media
import trailer_park

#For each movie, pass its IMDb ID and Youtube trailer link
#(Consider revising this to just be a Youtube ID?)

movies = [
	media.Movie("tt0443455","https://www.youtube.com/watch?v=uNrgu8DO7-w"), #Brand upon the brain
	media.Movie("tt1182345","https://www.youtube.com/watch?v=E-E13MP3o54"), #Moon
	media.Movie("tt0076759","https://www.youtube.com/watch?v=1g3_CFmnU7k"), #Star Wars
	media.Movie("tt0050086","https://www.youtube.com/watch?v=AyDdnqYxhd8"), #3:10 to Yuma
	media.Movie("tt0105695","https://www.youtube.com/watch?v=XDAXGILEdro"), #Unforgiven
	media.Movie("tt0335266","https://www.youtube.com/watch?v=sU0oZsqeG_s"), #Lost in Translation
	media.Movie("tt0780504","https://www.youtube.com/watch?v=CWX34ShfcsE"), #Drive
	media.Movie("tt0087469","https://www.youtube.com/watch?v=HOwWfns4qqw"), #Indiana Jones and the Temple of Doom
	media.Movie("tt0056443","https://www.youtube.com/watch?v=ZHIRcbAMFHo"), #Sanjuro
	media.Movie("tt0091042","https://www.youtube.com/watch?v=R-P6p86px6U"), #Ferris Bueller's Day Off
	media.Movie("tt0910936","https://www.youtube.com/watch?v=_GnV2u30oOU"), #Pineapple Express
	media.Movie("tt0262432","https://www.youtube.com/watch?v=shVmpGH-YxA"), #George Washington
	media.Movie("tt0074174","https://www.youtube.com/watch?v=sF6De-XP7x4"), #Bad News Bears
	media.Movie("tt0356721","https://www.youtube.com/watch?v=2eOLOmCjRPY"), #I Heart Huckabees
	media.Movie("tt0365748","https://www.youtube.com/watch?v=yfDUv3ZjH2k"), #Shaun of the Dead
	media.Movie("tt0393109","https://www.youtube.com/watch?v=uM7E0XGiyrc"), #Brick
	media.Movie("tt0206634","https://www.youtube.com/watch?v=Q9CFcTY_pik"), #Children of Men
	media.Movie("tt0416320","https://www.youtube.com/watch?v=wISRAOb6xm0"), #Match Point
	media.Movie("tt0243759","https://www.youtube.com/watch?v=rikiGMGhKVw"), #The American Astronaut
	media.Movie("tt0050613","https://www.youtube.com/watch?v=PoYzsDVyFRU"), #Throne of Blood
	media.Movie("tt0061747","https://www.youtube.com/watch?v=0Eh-FOdu5ho"), #Hang 'em High
	media.Movie("tt0119107","https://www.youtube.com/watch?v=jPbdwsZh38o"), #Fast, Cheap & Out of Control
	media.Movie("tt0070334","https://www.youtube.com/watch?v=GeNyD9UFXHs"), #The Long Goodbye
	media.Movie("tt0056869","https://www.youtube.com/watch?v=LrN_U830_Gc"), #The Birds
	media.Movie("tt0443680","https://www.youtube.com/watch?v=-FsN_utDELE"), #The Assassination of Jesse James by the Coward Robert Ford
	media.Movie("tt0118799","https://www.youtube.com/watch?v=16RZHqCIy9M"), #Life is Beautiful
	media.Movie("tt0379217","https://www.youtube.com/watch?v=P_7uQsP2TBk"), #Coffee and Cigarettes
	media.Movie("tt0038355","https://www.youtube.com/watch?v=VjJlBnfyiI4"), #The Big Sleep
	media.Movie("tt0091167","https://www.youtube.com/watch?v=Qtgw38Yq2Qs"), #Hannah and Her Sisters
	media.Movie("tt0103905","https://www.youtube.com/watch?v=bcPhaieTg4o"), #Man Bites Dog
	media.Movie("tt0266697","https://www.youtube.com/watch?v=ot6C1ZKyiME"), #Kill Bill
	media.Movie("tt0079470","https://www.youtube.com/watch?v=tOOVm4kY4lE"), #Life of Brian
	media.Movie("tt0068646","https://www.youtube.com/watch?v=sY1S34973zA"), #The Godfather
	media.Movie("tt0047478","https://www.youtube.com/watch?v=MwvpUtc1hBU"), #Seven Samurai
	media.Movie("tt0057012","https://www.youtube.com/watch?v=1gXY3kuDvSU"), #Dr. Strangelove
	media.Movie("tt0071315","https://www.youtube.com/watch?v=3aifeXlnoqY"), #Chinatown
]

trailer_park.open_movies_page(movies)