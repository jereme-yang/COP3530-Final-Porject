from GenerateArtists import generate_artist_list
from random import shuffle
from SortingAlgorithms import mergeSort, quickSort, quickSortIt
from SimlarityAlgo import get_similarity_score
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
    related_artists = sp.artist_related_artists(current_artist.get_id())['artists']
    if not related_artists:
        current_index -= 1
        continue

    related_artist = {
    'name': related_artists[randint(0, len(related_artists) - 1)]['name'],
    'id': related_artists[randint(0, len(related_artists) - 1)]['id']
    }
    nearby_index = current_index + randint(1, 10)
    while nearby_index < 0 or nearby_index >= len(artist_list) or nearby_index == current_index:
        nearby_index = current_index + randint(1, 10)
    nearby_artist = {
    'name': artist_list[nearby_index].get_name(),
    'id': artist_list[nearby_index].get_id()
    }
    options = [related_artist, nearby_artist]
    shuffle(options)
    print(f'LEVEL : {level}\nNAME OF ARTIST : {current_artist.get_name()}\n')
    
    option1_score = get_similarity_score(current_artist.get_id(), options[0]['id'])
    option2_score = get_similarity_score(current_artist.get_id(), options[1]['id'])

    if option1_score > option2_score:
        correct_option = "1"
        print("Option 1: " + options[0]['name'])
        print("Option 2: " + options[1]['name'])
    else:
        correct_option = "2"
        print("Option 1: " + options[1]['name'])
        print("Option 2: " + options[0]['name'])
    user_input = input("type 1 for option 1 and 2 for option 2: ")
    if (user_input == correct_option):
        score += 1
        level += 1
        current_index -= randint(1, 100)
    else:
        has_lost = True
        print("you lost! Your final score: " + str(score))


