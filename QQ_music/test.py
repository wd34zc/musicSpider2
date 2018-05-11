
from urllib import parse

from QQ_music.util.url_util import UrlUtil

song = "告白气球 周杰伦"

UrlUtil.get_client_search(parse.quote(song))
url_song = parse.quote(song)
print(url_song)

