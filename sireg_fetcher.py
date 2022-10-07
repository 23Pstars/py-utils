#!/usr/bin/python

import os.path
import urllib

src = '/home/zaf/Nextcloud/bank/bri/20221/foto/foto.csv'
dst = '/home/zaf/Nextcloud/bank/bri/20221/foto/'

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
    urllib.urlretrieve(__user[1], __dest)
    print(__user[1])
    # print(dst + __user[0] + '.' + __photo[-1])
