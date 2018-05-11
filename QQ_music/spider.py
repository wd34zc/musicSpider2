import json
import re
from urllib import request, parse
from QQ_music.util.url_util import UrlUtil


class QQMusicSpider:
    @staticmethod
    def search(song):
        html = QQMusicSpider.QQ_music_spider(song)
        # mid = QQMusicSpider.get_music_id(html)
        mid = QQMusicSpider.select_music_id(html)
        url = UrlUtil.get_music_home(mid)
        print(url)
        return url

    @staticmethod
    def QQ_music_spider(song):
        # song = "告白气球 周杰伦"
        url_song = parse.quote(song)
        url = UrlUtil.get_client_search(url_song)
        req = request.Request(url=url)
        response = request.urlopen(req).read()
        html = response.decode("utf-8")
        # print(html)
        return html

    @staticmethod
    def get_music_id(html):
        result = re.match("[\w']*\(({[\w\W]*})\)", html).group(1)
        # print(result)
        data = json.loads(result, strict=False)
        mid = data['data']['song']['list'][00]['mid']
        print(mid)
        return mid

    @staticmethod
    def select_music_id(html):
        result = re.match("[\w']*\(({[\w\W]*})\)", html).group(1)
        # print(result)
        data = json.loads(result, strict=False)
        song_list = data['data']['song']['list']
        QQMusicSpider.show_music(song_list)
        flag = 0
        while flag is 0:
            try:
                index = input("请选择要下载的歌曲序号：")
                index = int(index)
                if len(song_list) < index:
                    raise ValueError
                mid = song_list[index]['mid']
                flag = 1
            except ValueError:
                print("请输入正确的歌曲序号。")
                print("退出直接关闭窗口。")
        print(mid)
        return mid

    @staticmethod
    def show_music(song_list):
        i = -1
        for song in song_list:
            i = i+1
            album = song['album']['name']
            title = song['title']
            singer = song['singer'][0]['name']
            print(str(i) + '  歌曲：【' + title + '】  歌手：【' + singer + "】  专辑：【" + album + '】');
