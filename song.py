#create Song class

class Song:
    def __init__(self, title="", artist="", year=0, is_required=""):
        self.artist = artist
        self.title = title
        self.year = year
        self.is_required = is_required

    #Check whether a song is learned or not
    def __str__(self):
        if self.is_required == "n":
            is_required = "learned"
            return ("You have learned {} by {} ({})".format(self.title,self.artist, self.year))
        else:
            is_required = "y"
            return ("You have not learned {} by {} ({})".format(self.title,self.artist, self.year))

    def mark_learned(self):
        #Mark the song learned
        self.is_required = 'n'
        return self.is_required
