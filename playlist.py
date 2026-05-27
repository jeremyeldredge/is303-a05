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
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist}"
    
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songlist = []

    def __str__(self):
        return f"{self.name} playlist with {len(self.songlist)} songs"
    
