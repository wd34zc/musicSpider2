class Song:
    singer = ''
    song = ''
    index = ''

    def __str__(self) -> str:
        return self.singer + " " + self.song + " " + self.index