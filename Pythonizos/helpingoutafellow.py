from collections import deque
class Song:
    def __init__(self):
        self.title = ""
        self.artist = ""

    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")

    def display(self):
        print("Playing song:")
        print(f"{self.title} by {self.artist}")


def main():
    playlist = deque()
    song = Song()
    option = 0
    while option != 4:
        print("Options: ")
        print("1. Add a song to the end of the playlist")
        print("2. Insert a new song to the beggining of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        option = input("Enter selection: ")
        if option == "1":
            print()
            song.prompt()
            playlist.append(song)
            print()
        elif option == "2":
            print()
            song.prompt()
            playlist.appendleft(song)
            print()
        elif option == "3":
            song = Song()
            print()
            playlist = playlist.popleft()
            song.display()


if __name__ == "__main__":
    main()