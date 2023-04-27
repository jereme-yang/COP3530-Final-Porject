import json

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from Artist import Artist
client_id = '024d2accff6645c7919e60466b8ec3f0'
client_secret = '2ed4211bd77444bf8f04f87508c4073c'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

genres = sp.recommendation_genre_seeds()['genres']
genre= genres[0]
genre_inc = 0
artist_set = []
query = 'genre:"pop"'
limit = 50
offset = 0
total_artists = 100000
artists = []
temp = {}
json_string = json.dumps(temp)
while len(artists) < total_artists:
    results = sp.search(q="genre:" + genre, type='artist', limit=limit, offset=offset)
    items = results['artists']['items']
    for item in items:

        if len(artists) == total_artists:
            break
        if artists.count(item['name']) == 0:
            json_string += "," + json.dumps(item, indent=10)
        artists.append(item['name'])
    offset += limit
    if offset == 1000:
        offset = 0
        genre_inc += 1
        genre = genres[genre_inc % len(genres)]


with open("data.json", "w") as json_file:
    json_file.write(json_string)

# Write the artists to a JSON file

    

