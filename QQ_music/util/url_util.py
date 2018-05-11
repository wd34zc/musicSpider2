class UrlUtil:
    @staticmethod
    def get_client_search(song):
        part1 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24" \
                "&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=45546156866255969&t=0&aggr=1&cr=1" \
                "&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w="
        part3 = "&g_tk=5381&jsonpCallback=MusicJsonCallback7295081134089829&loginUin=568948382&hostUin=0&format=jsonp" \
                "&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"

        # part2 = "告白气球 周杰伦"
        part2 = song
        url = part1 + part2 + part3
        # print(url)
        return url

    @staticmethod
    def get_smart_box(song):
        part1 = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?is_xml=0&format=jsonp&key="
        part2 = ""
        part3 = "&g_tk="
        part4 = "104710228"
        part5 = "&jsonpCallback=SmartboxKeysCallbackmod_search6085"
        part6 = "&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"

        part2 = "告白气球 周杰伦"
        part2 = song
        url = part1 + part2 + part3 + part4 + part5 + part6

        # print(url)
        return url

    @staticmethod
    def get_music_home(song_id):
        part1 = "https://y.qq.com/n/yqq/song/"
        part3 = ".html"

        part2 = "002KZ58u4DHUMf"
        part2 = song_id

        url = part1 + part2 + part3
        # print(url)
        return url

