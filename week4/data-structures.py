from collections import deque

"""Create a Song class that has member variables for a title and an artist. 
It should have a prompt function that asks the user for the title and artist, 
and a display function that displays the title and the artist to the screen."""


class Song:

    def __init__(self):
        self.title = ''
        self.artist = ''

    def prompt(self):
        self.title = input('Enter the title: ')
        self.artist = input('Enter the artist: ')
        print()

    def display(self):
        print('It comes fro the Display member method')
        print('Playing song: ')
        print(f'{self.title} by {self.artist}')
        print()


def main():
    playlist = deque()
    option = 0
    while option != 4:
        print('Options: ')
        print('1. Add a new song to the end of the playlist')
        print('2. Insert a new song to the beginning of the playlist ')
        print('3. Play the next song ')
        print('4. Quit ')
        option = int(input('Enter a selection: '))
        print()
        if option == 4:
            print('Good bye')
            break
        if option == 1:
            song = Song()
            song.prompt()
            playlist.append(song)
        if option == 2:
            song = Song()
            song.prompt()
            playlist.appendleft(song)
        if option == 3:
            if len(playlist) == 0:
                print('The playlist is empty cv, llénala.')
                print()
                # continue will take it back to the while loop.
                continue
            # in case that the list is full, it will play it.

            playlist.pop().display()
            print('')


if __name__ == '__main__':
    main()
