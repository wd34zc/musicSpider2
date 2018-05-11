part1 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24" \
        "&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=45546156866255969&t=0&aggr=1&cr=1" \
        "&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w="
part3 = "&g_tk=5381&jsonpCallback=MusicJsonCallback7295081134089829&loginUin=568948382&hostUin=0&format=jsonp" \
        "&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"

part2 = "告白气球 周杰伦"
url = part1 + part2 + part3
print(url)