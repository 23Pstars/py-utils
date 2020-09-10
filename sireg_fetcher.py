#!/usr/bin/python

import os.path
import urllib

src = '/Users/zaf/Sites/unram/sireg/_sql/photos/foto_pascasarjana.csv'
dst = '/Users/zaf/Sites/unram/sireg/_sql/photos/pascasarjana/'

with open(src) as _content:
    contents = _content.readlines()

photos = [i.strip().replace('"', '') for i in contents]

for _user in photos:
    __user = _user.split(',')
    __photo = __user[1].split('.')
    if len(__photo) >= 4:
        __dest = dst + __user[0] + '.' + __photo[4]
        if os.path.exists(__dest):
            continue
        urllib.urlretrieve(__user[1], __dest)
        print(__user[1])
        # print(dst + __user[0] + '.' + __photo[4])
