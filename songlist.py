# create your SongList class
from song import Song               #import Song class
from operator import attrgetter     #import ttribute Getter


class SongList:


    def __init__(self):
        self.list_songs = []

    def load_songs(self):

        #Load the csv file
        #open the file

        in_file = open("songs.csv","r")
        lines = in_file.readlines()
        for line in lines:
            song_item = line.split(',')
            song_item[3] = song_item[3].strip('\n')
            loaded_song = Song(song_item[0],song_item[1],song_item[2],song_item[3])

            # self.list_songs.append(loaded_song)
            self.list_songs.append(loaded_song)

        #close the file
        in_file.close()


    def sort(self, key):
        """
        Sort the songs based on the sort_choice selected
        :param key: self, key
        :return: none
        """
        self.list_songs = sorted(self.list_songs, key=attrgetter(key, "title"))

    def add_to_list(self, title, artist, year, is_required):
        #add the inputted song to the song list
        newSong = Song(title, artist, year, 'y')
        self.list_songs.append(newSong)


    def save_songs(self):
        #save changes made to the songs and then out file
        csv_string = ""
        for each in self.list_songs:
            csv_string += "{},{},{},{}\n".format(each.title, each.artist, each.year, each.status)
        out_file = open("songs.csv", 'w')
        out_file.seek(0)
        out_file.truncate()
        out_file.write(csv_string)
        out_file.close() #close the file




