#!/usr/bin/python3.8

import os.path
import urllib.request

src = '/home/zaf/Downloads/foto/snbt/foto.csv'
dst = '/home/zaf/Downloads/foto/snbt/'

with open(src) as _content:
    contents = _content.readlines()

photos = [i.strip().replace('"', '') for i in contents]

for _user in photos:
    __user = _user.split(',')
    __photo = __user[1].split('.')
    __dest = dst + __user[0] + '.' + __photo[-1]
    if os.path.exists(__dest):
        continue
    if __user[1] == '':
        continue
    urllib.request.urlretrieve(__user[1], __dest)
    print(__user[1])
    # print(dst + __user[0] + '.' + __photo[-1])
