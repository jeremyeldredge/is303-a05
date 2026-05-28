"""
Is 303 A05 - Jeremy Eldredge
Playlist Maker

Inputs:
- song (title, artist, duration)

Processes:
- class: Playlist
    - compile all songs into a list (playlist)
    - calculate total duration
    - find longest song
    - shuffle order of songs and display
- class: Song
    - collect song title, artist, and duration
    - display song as string
    - check if song is longer than 5 min

Outputs:
- playlist in shuffled order
"""

class Song:
    def __init__(self,title,artist,seconds):
        self.title = title
        self.artist = artist
        self.seconds = seconds

    def __str__(self):
        return f"{self.title} by {self.artist}"
    
    def long_song(self):
        return self.seconds > 300
    

    
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songlist = []

    def __str__(self):
        return f"Your playlist titled '{self.name}' has {len(self.songlist)} songs. Total duration: {format_duration(self.total_duration())} \n{self.convert_playlist_to_string()} \nLongest song: {self.longest_song()}"
    

    def total_duration(self):
        duration = 0
        for song in self.songlist:
            duration += song.seconds
        return duration
    
    def longest_song(self):
        longest = self.songlist[0]
        for song in self.songlist:
            if song.seconds > longest.seconds:
                longest = song
        return longest

    def shuffle_playlist(self):
        import random
        random.shuffle(self.songlist)
        return self.songlist
    
    def convert_playlist_to_string(self):
        playlist_str = ""
        for song in self.songlist:
            playlist_str += f"{song.title} by {song.artist} ({format_duration(song.seconds)})\n"
        return playlist_str
    

def format_duration(seconds):
    return f"{seconds // 60}:{seconds % 60:02d}"

 # --- Main Flow ---

playlist_1 = Playlist("Oldies but Goodies")

# song durations are input as total seconds, output formats into minutes and seconds
song_1 = Song("Dance The Night Away", "Van Halen", 188)
song_2 = Song("Take The Money And Run", "Steve Miller Band", 125)
song_3 = Song("(Dont Fear) The Reaper", "Blue Oyster Cult", 308)
song_4 = Song("Take It Easy","Eagles",211)

playlist_1.songlist.append(song_1)
playlist_1.songlist.append(song_2)
playlist_1.songlist.append(song_3)
playlist_1.songlist.append(song_4)

playlist_1.shuffle_playlist()
print(playlist_1)
