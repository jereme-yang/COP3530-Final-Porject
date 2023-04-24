from GenerateArtists import generate_artist_list
from SortingAlgorithms import mergeSort, quickSort, quickSortIt
from time import sleep
from random import randint
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import ascii


client_id = '024d2accff6645c7919e60466b8ec3f0'
client_secret = '2ed4211bd77444bf8f04f87508c4073c'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

ascii.welcome()
sleep(2)
ascii.loadingIP()
with open("data.json") as file:
    artist_list = json.load(file)
artist_list = generate_artist_list(artist_list)
# organize data
ascii.loadingComplete()

sortingAlg = ""
while sortingAlg != '1' and sortingAlg != '2':

    sortingAlg = input("choose 1 for quicksort and 2 for mergesort: ")

    match sortingAlg:
        case "1":
            quickSortIt(artist_list, 0, len(artist_list)-1)
        case "2": 
            mergeSort(artist_list, 0, len(artist_list)-1)

#begin game mechanics
score = 0
level = 0
has_lost = False
current_index = len(artist_list) - randint(1, 100)
while (not has_lost):
    current_artist = artist_list[current_index]
    options = sp.artist_related_artists(current_artist.get_id())['artists'][:2]
    while len(options) != 2:
        current_index -= 1
        current_artist = artist_list[current_index]
        options = sp.artist_related_artists(current_artist.get_id())['artists'][:2]
    print(f'LEVEL : {level}\nNAME OF ARTIST : {current_artist.get_name()}\n')
    
    random_index = randint(0, 1)
    correct_option = "1" if random_index == 0 else "2"
    if (correct_option == "1"):
        print("Option 1: "+ options[0]['name'])
        print("Option 2: "+ options[1]['name'])
    else:
        print("Option 1: "+ options[1]['name'])
        print("Option 2: "+ options[0]['name'])
    user_input = input("type 1 for option 1 and 2 for option 2: ")
    if (user_input == correct_option):
        score += 1
        level += 1
        current_index -= randint(1, 100)
    else:
        has_lost = True
        print("you lost! Your final score: " + str(score))


