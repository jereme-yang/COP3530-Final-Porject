

#artist object
#popularity and followers stored to calculate the artists' difficulty rating
class Artist:
    def __init__(self, id, name, popularity, genres, href, images, followers):
        self.id = id #used 
        self.name = name #used
        self.popularity = popularity #used
        self.genres = genres
        self.href = href
        self.images = images
        self.followers = followers #used


    #/==========ACCESSORS==========/
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_obscurity_rating(self): #used in sorting artist objects by difficulty in merge/quick sort
        return self.popularity * self.followers // 100
    

    