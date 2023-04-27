from GenerateArtists import generate_artist_list
from SortingAlgorithms import mergeSort, quickSortIt
from SimlarityAlgo import get_similarity_score
from random import randint, shuffle
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '024d2accff6645c7919e60466b8ec3f0'
client_secret = '2ed4211bd77444bf8f04f87508c4073c'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_list_global = []

def initialize_game(genre_file, sorting):
    global artist_list_global
    
    # Load the JSON file and generate the artist list
    with open("./data/" + genre_file) as file:
        artist_list_data = json.load(file)

    artist_list_global = generate_artist_list(artist_list_data)
    
    if sorting == '1':
        quickSortIt(artist_list_global, 0, len(artist_list_global) - 1)
    elif sorting == '2':
        mergeSort(artist_list_global, 0, len(artist_list_global) - 1)

    current_index = len(artist_list_global) - randint(1, 30)
    level = 0
    has_lost = False
    game_state = game_logic(current_index, level, has_lost)
    return game_state

def game_logic(current_index, level, has_lost):
    global artist_list_global
    if has_lost:
        return {
            'current_index': current_index,
            'level': level,
            'has_lost': has_lost
        }
    current_artist = artist_list_global[current_index]
    related_artists = sp.artist_related_artists(current_artist.get_id())['artists']
    if not related_artists:
        current_index -= 1
        return {
            'current_index': current_index,
            'level': level,
            'has_lost': has_lost
        }

    related_artist_index = randint(0, len(related_artists) - 1)  # Generate a single random index
    embed = f"https://open.spotify.com/embed/artist/{related_artists[related_artist_index]['id']}?utm_source=generator"   
    related_artist = {
        'name': related_artists[related_artist_index]['name'],
        'id': related_artists[related_artist_index]['id'],
        'embed': embed,
    }

    nearby_index = current_index + randint(1, 10)
    while nearby_index < 0 or nearby_index >= len(artist_list_global) or nearby_index == current_index:
        nearby_index = current_index - randint(1, 10)
    nearby_artist = {
        'name': artist_list_global[nearby_index].get_name(),
        'id': artist_list_global[nearby_index].get_id(),
        'embed' : artist_list_global[nearby_index].get_href(),
    }

    options = [related_artist, nearby_artist]
    shuffle(options)

    scores = []
    for option in options:
        score = get_similarity_score(current_artist.get_id(), option['id'])
        scores.append(score)

    #print("Similarity score between {} and {}: {}".format(current_artist.get_name(), options[0]['name'], scores[0]))  # Add this line
    #print("Similarity score between {} and {}: {}".format(current_artist.get_name(), options[1]['name'], scores[1]))  # Add this line

    if scores[0] > scores[1]:
        correct_option = "1"
    else:
        correct_option = "2"

    current_artist = artist_list_global[current_index]
    game_state = {
        'current_index': current_index,
        'level': level + 1,
        'has_lost': has_lost,
        'current_artist': current_artist.to_dict(),
        'options': options,
        'correct_option': correct_option,
    }

    print("Game state in game_logic:", game_state)  # Add this line

    return game_state