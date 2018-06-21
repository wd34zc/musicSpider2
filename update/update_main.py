import threading

from QQ_music.spider import QQMusicSpider
from music_search.spider import MusicSearchSpider
from update.entity import Song
from update.io_util import IOUtil

thread_list = []

conf = IOUtil.read_conf()
path = conf.get('update_path')
buffer = conf.get('buffer_path')

songs = IOUtil.read_music_list(path)
songs = Song.read_song_list(songs)

# song = Song.create('告白气球', '周杰伦')
music_urls = QQMusicSpider.update_search(songs)

for u in music_urls:
    t = threading.Thread(target=MusicSearchSpider.music_search_spider, args=(u, buffer, False))
    t.start()
    thread_list.append(t)
    if len(thread_list) > 4:
        thread_list.pop().join()
        thread_list.clear()

# thread_list.pop().join()
del thread_list

IOUtil.move(buffer, path)
