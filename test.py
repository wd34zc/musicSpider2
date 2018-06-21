import os
import shutil

from update.entity import Song
from update.io_util import IOUtil

path = 'z:/music'
# path = 'F:\QQ栋'
# for dir in os.listdir(path):
#     print(dir)
#     size = os.path.getsize('%s/%s' % (path, dir))
#     print(size)

l = IOUtil.read_music_list(path)
print(l)
# l2 = Song.read_song_list(l)
# print(l2)
# string = '韩红,林俊杰 - 飞云之下.mp3'
# song = string[:-4]
# s = song.split(' - ')
# print(s)

os.remove('z:/aab.txt')
shutil.move('z:/buffer/aab.txt', 'z:/')
# os.rename('z:/buffer/aaa.txt', 'z:/buffer/aab.txt')