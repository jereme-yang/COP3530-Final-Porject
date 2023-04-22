

#artist object
#popularity and followers stored to calculate the artists' difficulty rating
class Artist:
    def __init__(self, id, name, popularity, genres, href, images, followers, top_track_id, related_artist_name_one, related_artist_id_one, related_artist_name_two, related_artist_id_two):
        self.id = id #used 
        self.name = name #used
        self.popularity = popularity #used
        self.genres = genres
        self.href = href
        self.images = images
        self.followers = followers #used
        self.top_track_id = top_track_id
        self.related_artist_name_one = related_artist_name_one #used
        self.related_artist_id_one = related_artist_id_one #used
        self.related_artist_name_two = related_artist_name_two #used 
        self.related_artist_id_two = related_artist_id_two #used

    #/==========ACCESSORS==========/
    def get_name(self):
        return self.name
    def get_related_artist_name_one(self):
        return self.related_artist_name_one
    def get_related_artist_name_two(self):
        return self.related_artist_name_two
    def get_obscurity_rating(self): #used in sorting artist objects by difficulty in merge/quick sort
        return self.popularity * self.followers // 100
    

    