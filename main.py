from QQ_music.spider import QQMusicSpider
from io_util import IOUtil
from music_search.spider import MusicSearchSpider

print("仅兼容QQ音乐，下载的歌曲默认为搜索词条的第一条。")
print("输入格式：歌曲名 歌手名")
print("例如：告白气球 周杰伦")
# str = input("请输入要下载的歌曲：")

conf = IOUtil.read_conf()
path = conf.get('path')
# music_url = QQMusicSpider.search(str)
music_url = QQMusicSpider.search('告白气球 周杰伦')
MusicSearchSpider.music_search_spider(music_url, path)

input("Press <enter>")
