from collections import deque


class Song:

    def __init__(self):
        self.title = ''
        self.artist = ''

    def prompt(self):
        self.title = input('Enter the title: ')
        self.artist = input('Enter the artist: ')

        playlist = deque()
        playlist.append(self.title)