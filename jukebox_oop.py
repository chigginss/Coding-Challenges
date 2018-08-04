""" Building a Jukebox 

    Needs a jukebox class, player class, playlist class, cds class, artists, songs, credits

    on Jukebox class, add methods to check credits, add credits, to show song, and to add song to queue(playlist)

"""

class Queue(object):

    def __init__(self, data=[]):
        self.data = data

    def deque(self):
        Queue.pop(0)

    def enque(self, item):
        Queue.append(item)

    def is_empty(self):
        if len(Queue) < 1:
            return True

    def peek(self):
        entity =  self.data[0]
            return entity

    def size(self):
        return len(self.data)

class Jukebox (object):

    def __init__(self, cds):
        self.Player = Player()
        self.cds = cds
        self.playlist = Playlist()
        self.credits = 0

    def play_song(playlist):
        if not self.playlist.is_empty() and self.has_credits():
            self.player.play(self.playlist.deque())
            credits -= 1

    def queue_song(self, song):
        if self.has_credits:
            self.playlist.enque(song)

    def has_credits(self):
        return self.credits > 0

    def add_credits(self):
        self.credits += 1

    def show_songs(self):
        for cd in cds:
            for song in cd.songs:
                print(song)

class Cds (object):

    def __init__(self, artist, name, songs, id):
        self.artist = artist
        self.songs = songs
        self.name = name
        self.id = id

class Artist (object):

    def __init__(self, name):
        self.name = name

class Song (object):

    def __init__(self, title):
        self.title = title

class Playlist (object):

    def __init__(self):
        playlist = new Queue()


