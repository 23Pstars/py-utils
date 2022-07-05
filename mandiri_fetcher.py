#!/usr/bin/python

import os.path
import urllib

src = '/home/zaf/Nextcloud/mandiri/20221/pernyataan/Pembayaran_20220705.csv'
dst = '/home/zaf/Nextcloud/mandiri/20221/pernyataan/'

with open(src) as _content:
    contents = _content.readlines()

_contents = [i.strip().replace('"', '') for i in contents]

for _row in _contents:
    _row = _row.split(',')

    __no_tes = _row[2]
    if __no_tes == '':
        continue

    __pil1 = _row[12]
    if __pil1 == '':
        continue

    ___pil1 = __pil1.split('.')

    if len(___pil1) <= 1:
        continue

    __pil1_dest = dst + __no_tes + '-p1.' + ___pil1[-1]
    if os.path.exists(__pil1_dest):
        continue

    urllib.urlretrieve(__pil1, __pil1_dest)
    print(__pil1_dest)

    __pil2 = _row[18]
    if __pil2 == '':
        continue

    ___pil2 = __pil2.split('.')

    if len(___pil2) <= 1:
        continue

    __pil2_dest = dst + __no_tes + '-p2.' + ___pil2[-1]
    if os.path.exists(__pil2_dest):
        continue

    urllib.urlretrieve(__pil2, __pil2_dest)
    print(__pil2_dest)
