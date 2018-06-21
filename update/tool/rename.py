import os


def rename(a, b):
    if os.path.exists(b):
        os.remove(a)
    else:
        os.rename(a, b)


spe = ['张惠妹 - 记得 - 林俊杰 不懂.mp3']

# path = 'F:/QQ栋'
path = 'I:/QQ栋'
buffer = 'z:/buffer'

dirs = os.listdir(path)
for d in dirs:
    if d in spe:
        continue

    pathh = path + '/'
    strs = d.split(' - ')

    if len(strs) == 2:
        continue
    elif len(strs) > 2:
        strs = d.split(' - ', 1)
        strss = strs[0]
        strs = strs[1]
        strs = strs.replace(' - ', '-')
        strs = '%s - %s' % (strss, strs)
        rename(pathh + d, pathh + strs)
        continue
    # 周杰伦-回到过去.mp3
    strs = d.split('-')
    l = len(strs)
    if l == 2:
        strs = '%s - %s' % (strs[0], strs[1])
        rename(pathh + d, pathh + strs)
        continue
