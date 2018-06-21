'''
通过urllib请求
'''
import json
from urllib import request, parse
import requests
from tqdm import tqdm

from download.io_util import IOUtil
from music_search.header import Header


class MusicSearchSpider:
    @staticmethod
    def music_search_spider(song_url, path, flag=True):
        html = MusicSearchSpider.spider1(song_url)

        url2, singer, song = MusicSearchSpider.parse(html)
        music_name = singer + ' - ' + song + '.mp3'
        if flag:
            if IOUtil.music_exist(path, music_name):
                print('歌曲：' + song + ' 已存在。')
                flag = input('是否覆盖[Y/N]')
                if flag is not 'y' and flag is not 'Y':
                    return
        if url2 is None:
            print(song + "获取下载连接失败。")
        # music = MusicSearchSpider.download_music_with_tqdm(url2, path, music_name)
        music = MusicSearchSpider.download_music(url2)
        print(song + ': 下载完毕:')
        IOUtil.save_music(path, music, music_name)

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
    def download_music_with_tqdm(url2, path, song):
        # req = requests.get(url2, stream=True)
        # length = req.headers['content-length']
        # response = req.content
        response = requests.get(url2, stream=True)
        print("\r文件总大小：" + response.headers['content-length'])
        # 用response储存在获取url的响应
        with open(path+'/'+song, "wb") as handle:
            # 打开本地文件夹路径filename，以二进制写入，命名为handle
            for data in tqdm(response.iter_content()):
                # tqdm进度条的使用,for data in tqdm(iterable)
                handle.write(data)
            # 在handle对象中写入data数据
        return response

    @staticmethod
    def download_music(url):
        req = requests.get(url)
        return req.content

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


