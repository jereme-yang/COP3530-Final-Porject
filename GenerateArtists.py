import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Artist import Artist

def generate_artist_list(artist_list):
    #connect to spotify api / spotipy
    client_id = '024d2accff6645c7919e60466b8ec3f0'
    client_secret = '2ed4211bd77444bf8f04f87508c4073c'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    genres = sp.recommendation_genre_seeds()['genres']

    # 10k artist objects in list, 10 data points per artist object = 100k data points
    while len(artist_list) < 10: # CHANGE TO 10K later

        random_genre = random.choice(genres)
        results = sp.search(q='genre:' + random_genre, type='artist')
        for artist in results['artists']['items']:

            #data points being stored in the artist object
            id = artist['id']
            name = artist['name']
            popularity = artist['popularity']
            genres = artist['genres']
            href = artist['href']
            images = artist['images']
            followers = artist['followers']['total']
            if (len(sp.artist_related_artists(id)['artists']) < 2): continue #ignore artists with no related artists
            top_track_id = sp.artist_top_tracks(id)['tracks'][0]['id']
            related_artist_name_one = sp.artist_related_artists(id)['artists'][0]['name']
            related_artist_id_one = sp.artist_related_artists(id)['artists'][0]['id']
            related_artist_name_two = sp.artist_related_artists(id)['artists'][1]['name']
            related_artist_id_two = sp.artist_related_artists(id)['artists'][1]['id']
                
            newArtist = Artist(id, name, popularity, genres, href, images, followers, top_track_id, related_artist_name_one, related_artist_id_one, related_artist_name_two, related_artist_id_two)

            artist_list.append(newArtist)
