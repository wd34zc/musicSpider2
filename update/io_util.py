import os
import shutil


class IOUtil:

    @staticmethod
    def read_conf():
        conf = {}
        file = open('configure.conf', 'r', encoding='UTF-8')
        for line in file:
            line = line.strip()
            if line[0:2] == "//":
                continue
            else:
                map = line.split('=')
                conf[map[0].strip()] = map[1].strip()
        file.close()
        # print(conf)
        return conf

    @staticmethod
    def get_path():
        conf = IOUtil.read_conf()
        path = conf.get("path")
        if path is None:
            print("配置文件没有配置path路径，音乐默认保存到运行文件的文件夹下。")
            path = os.getcwd()
        else:
            if os.path.isdir(path) is not True:
                print("配置文件path路径不是文件夹，请检查路径是否正确。")
            else:
                print("获取到路径：" + path)
        return path

    @staticmethod
    def music_exist(path, song_name):
        return os.path.exists(path + '/' + song_name)

    @staticmethod
    def save_music(path, music, music_name):
        f = open(path + '/' + music_name, "wb")
        f.write(music)
        f.close()
        print('保存完毕：' + music_name + ' ' + path)

    @staticmethod
    def read_music_list(path):
        song_list = []
        if not os.path.exists(path):
            return song_list
        for song in os.listdir(path):
            if song.endswith('.mp3'):
                # song = '%s/%s'%(path, song)
                if os.path.getsize('%s/%s' % (path, song)) < 5 * 1024 * 1024:
                    song_list.append(song)
        return song_list

    @staticmethod
    def move(buffer, path):
        buffers = os.listdir(buffer)
        for m in buffers:
            n_file = '%s/%s' % (buffer, m)
            o_file = '%s/%s' % (path, m)
            if os.path.exists(o_file):
                n_size = os.path.getsize(n_file)
                o_size = os.path.getsize(o_file)
                if n_size > o_size:
                    os.remove(o_file)
                    shutil.move(n_file, path)
