import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import itertools
import math
import numpy as np

# Replace with your own credentials
client_id = 'b3d2a86c81d74b16a01363644d6a131b'
client_secret = 'f8d5f7a742bd4c7d97a9871b8492d78d'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_id_popularity_and_genres(name):
    result = sp.search(q='artist:' + name, type='artist')
    artist = result['artists']['items'][0]
    return artist['id'], artist['popularity'], artist['genres']

# Function to get related artists
def get_related_artists(artist_id):
    return [a['id'] for a in sp.artist_related_artists(artist_id)['artists']]

# Function to get artist name by ID
def get_artist_name(artist_id):
    artist = sp.artist(artist_id)
    return artist['name']

# Function to get playlist co-occurrence
def get_playlist_cooccurrence(artist1_id, artist2_id, limit=50):
    artist1_name = get_artist_name(artist1_id)
    artist2_name = get_artist_name(artist2_id)
    query = f'"{artist1_name}" AND "{artist2_name}"'
    results = sp.search(query, type='playlist', limit=limit)
    return results['playlists']['total']

# Function to create binary vectors
def create_binary_vector(elements, combined_set):
    binary_vector = [1 if element in elements else 0 for element in combined_set]
    return binary_vector

# Function to calculate cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2 + 1e-8)

def split_genres(genres):
    splitted_genres = set()
    for genre in genres:
        splitted_genres.update(genre.split())
    return splitted_genres

# Algorithm to calculate similarity score
def calculate_similarity_score(artist1_genres, artist2_genres, artist1_related_artists, artist2_related_artists, artist1_popularity, artist2_popularity, playlist_cooccurrence, genre_weight=.4, related_artists_weight=.2, popularity_weight=.1, playlist_cooccurrence_weight=0.3):
    # Normalize the weights
    total_weight = genre_weight + related_artists_weight + popularity_weight + playlist_cooccurrence_weight
    genre_weight /= total_weight
    related_artists_weight /= total_weight
    popularity_weight /= total_weight
    playlist_cooccurrence_weight /= total_weight

    combined_genres = list(set(artist1_genres).union(set(artist2_genres)))
    combined_related_artists = list(set(artist1_related_artists).union(set(artist2_related_artists)))

    artist1_genre_vec = create_binary_vector(artist1_genres, combined_genres)
    artist2_genre_vec = create_binary_vector(artist2_genres, combined_genres)

    artist1_related_artist_vec = create_binary_vector(artist1_related_artists, combined_related_artists)
    artist2_related_artist_vec = create_binary_vector(artist2_related_artists, combined_related_artists)

    genre_similarity = cosine_similarity(artist1_genre_vec, artist2_genre_vec)
    related_artists_similarity = cosine_similarity(artist1_related_artist_vec, artist2_related_artist_vec)
    popularity_similarity = 1 - abs(artist1_popularity - artist2_popularity) / 100

    return genre_weight * genre_similarity + related_artists_weight * related_artists_similarity + popularity_weight * popularity_similarity + playlist_cooccurrence_weight * (playlist_cooccurrence / 100)

if __name__ == "__main__":
    artist1_name = input("Enter the name of the first artist: ")
    artist2_name = input("Enter the name of the second artist: ")

    artist1_id, artist1_popularity, artist1_genres = get_artist_id_popularity_and_genres(artist1_name)
    artist2_id, artist2_popularity, artist2_genres = get_artist_id_popularity_and_genres(artist2_name)

    artist1_splitted_genres = split_genres(artist1_genres)
    artist2_splitted_genres = split_genres(artist2_genres)

    artist1_related_artists = get_related_artists(artist1_id)
    artist2_related_artists = get_related_artists(artist2_id)
    playlist_cooccurrence = get_playlist_cooccurrence(artist1_id, artist2_id)

    print(f"Playlist cooccurrence for {artist1_name} and {artist2_name}: {playlist_cooccurrence}")

    similarity_score = calculate_similarity_score(artist1_splitted_genres, artist2_splitted_genres, artist1_related_artists, artist2_related_artists, artist1_popularity, artist2_popularity, playlist_cooccurrence)
    print(f"Similarity score between {artist1_name} and {artist2_name}: {similarity_score:.2f}")