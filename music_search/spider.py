'''
通过urllib请求
'''
import json
import os
from urllib import request, parse

from io_util import IOUtil
from music_search.header import Header


class MusicSearchSpider:
    @staticmethod
    def music_search_spider(song_url, path):
        html = MusicSearchSpider.spider1(song_url)

        url2, singer, song = MusicSearchSpider.parse(html)
        music_name = singer + ' - ' + song + '.mp3'
        if IOUtil.music_exist(path, music_name):
            print('歌曲：' + song + ' 已存在。')
            flag = input('是否覆盖[Y/N]')
            if flag is not 'y' and flag is not 'Y':
                return
        if url2 is None:
            print(song + "获取下载连接失败。")
        music = MusicSearchSpider.spider2(url2)
        print(song + ': 下载完毕:')
        IOUtil.save_music(path, music, music_name)

    @staticmethod
    def music_search_spider2(song_url, path):
        html = MusicSearchSpider.spider1(song_url)

        url2, singer, song = MusicSearchSpider.parse(html)
        if url2 is None:
            print(song + "获取下载连接失败。")
        music = MusicSearchSpider.spider2(url2)
        music_name = singer + ' - ' + song + '.mp3'
        f = open(path + '/' + music_name, "wb")
        f.write(music)
        f.close()
        print('保存完毕：' + path + '/' + music_name )

    @staticmethod
    def music_search_spider3(song_url, path):
        html = MusicSearchSpider.spider1(song_url)

        url2, singer, song = MusicSearchSpider.parse(html)
        music_name = singer + ' - ' + song + '.mp3'
        if url2 is None:
            print(song + "获取下载连接失败。")
        music = MusicSearchSpider.spider2(url2)
        print(song + ': 下载完毕:')
        IOUtil.save_music(path, music, music_name)
        return music_name

    @staticmethod
    def spider1(song_url):
        url = u"http://www.guqiankun.com/tools/music/"
        post_data = {u'input': song_url,
                     u'filter': u'url',
                     u'type': u'_',
                     u'page': u'1'}
        headers = {u'X-Requested-With': Header.x_requested_with}
        data = parse.urlencode(post_data).encode('utf-8')
        req = request.Request(url=url, headers=headers, data=data)
        response = request.urlopen(req).read()
        html = response.decode('gbk')
        return html

    @staticmethod
    def spider2(url2):
        req = request.Request(url2)
        response = request.urlopen(req).read()
        return response


    @staticmethod
    def parse(data_str):
        data = json.loads(data_str, strict=False)
        music_msg = data['data'][0]
        url = music_msg['url']
        singer = music_msg['author']
        title = music_msg['title']
        print(singer + " " + title)
        # print(url)
        return url, singer, title


