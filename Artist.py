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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'popularity': self.popularity,
            'genres': self.genres,
            'href': self.href,
            'images': self.images,
            'followers': self.followers,
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id'],
            data['name'],
            data['popularity'],
            data['genres'],
            data['href'],
            data['images'],
            data['followers'],
        )

    #/==========ACCESSORS==========/
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_obscurity_rating(self): #used in sorting artist objects by difficulty in merge/quick sort
        return self.popularity * self.followers // 100
    def get_href(self):
        return self.href
