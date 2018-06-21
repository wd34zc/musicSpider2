class Song:
    singer = ''
    title = ''
    index = ''
    size = ''

    @staticmethod
    def create(title, singer, size=None):
        song = Song()
        song.size = size
        song.title = title
        song.singer = singer
        return song

    @staticmethod
    def read_song_list(music_list):
        song_list = []
        for song in music_list:
            strs = song[:-4]
            strs = strs.split(' - ')
            if len(strs) == 2:
                title = strs[1]
                singer = strs[0]
                song_list.append(Song.create(title, singer))
            else:
                print('格式错误：%s' % song)
        return song_list

    def __str__(self) -> str:
        return self.singer + " " + self.title + " " + self.index
