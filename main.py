import requests
import random

client_id = '024d2accff6645c7919e60466b8ec3f0'
client_secret = '2ed4211bd77444bf8f04f87508c4073c'

auth_url = 'https://accounts.spotify.com/api/token'

auth_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

auth_response = requests.post(auth_url, data=auth_data)
access_token = auth_response.json()['access_token']

def get_artist_info(artist_id, access_token):
    artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(artist_url, headers=headers)
    return response.json()
def get_top_tracks_playlist_id(access_token):
    browse_url = 'https://api.spotify.com/v1/browse/categories/toplists/playlists'
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'limit': 1}

    response = requests.get(browse_url, headers=headers, params=params)
    return response.json()['playlists']['items'][0]['id']

def get_artists_from_playlist(playlist_id, access_token):
    tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'limit': 100}

    response = requests.get(tracks_url, headers=headers, params=params)
    return [track['track']['artists'][0]['id'] for track in response.json()['items']]

def get_related_artists_with_popularity(artist_id, access_token):
    related_url = f'https://api.spotify.com/v1/artists/{artist_id}/related-artists'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(related_url, headers=headers)
    return {artist['id']: artist['popularity'] for artist in response.json()['artists']}


playlist_id = get_top_tracks_playlist_id(access_token)
top_artists_ids = get_artists_from_playlist(playlist_id, access_token)

random_artist_id = random.choice(top_artists_ids)
related_artists = get_related_artists_with_popularity(random_artist_id, access_token)

random_artist_info = get_artist_info(random_artist_id, access_token)
print(f"Original Artist: {random_artist_info['name']} (ID: {random_artist_info['id']}), Popularity: {random_artist_info['popularity']}")

# Sort the related artists by popularity in descending order and get the top 2 artists
top_related_artists = sorted(related_artists.items(), key=lambda x: x[1], reverse=True)[:2]

for artist_id, popularity in top_related_artists:
    artist_info = get_artist_info(artist_id, access_token)
    print(f"Related Artist: {artist_info['name']} (ID: {artist_info['id']}), Popularity: {popularity}")