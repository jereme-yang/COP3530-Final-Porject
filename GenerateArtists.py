from Artist import Artist


def generate_artist_list(artist_list):
    current_index = 0
    newList = []
    for artist in artist_list: # CHANGE TO 10K later
    
        #data points being stored in the artist object
        id = artist['id']
        name = artist['name']
        popularity = artist['popularity']
        genres = artist['genres']
        href = f"https://open.spotify.com/embed/artist/{id}?utm_source=generator"        
        images = artist['images']
        followers = artist['followers']['total']

        newArtist = Artist(id, name, popularity, genres, href, images, followers)
        newList.append(newArtist)
    return newList


    
