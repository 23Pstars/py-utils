#!/usr/bin/python

import os.path
from sqlite3 import Row
import urllib.request

# src = 'O:\\My Drive\\PUSTIK\\Audit\\2022\\14\\Pembayaran_2022_Pil1_Pendidikan_Dokter.csv'
# src = 'O:\\My Drive\\PUSTIK\\Audit\\2022\\14\\Pembayaran_2022_Pil2_Pendidikan_Dokter.csv'
# src = 'O:\\My Drive\\PUSTIK\\Audit\\2022\\14\\Pembayaran_2022_Pil1_Farmasi.csv'
# src = 'O:\\My Drive\\PUSTIK\\Audit\\2022\\14\\Pembayaran_2022_Pil2_Farmasi.csv'
# dst = 'O:\\My Drive\\PUSTIK\\Audit\\2022\\14\\pernyataan peserta\\'

src = 'O:\\My Drive\\PUSTIK\\Audit\\2022\\14\\Peserta_Mandiri_2022_Lulus.csv'
dst = 'O:\\My Drive\\PUSTIK\\Audit\\2022\\14\\peserta lulus\\'

# p = '1'
# p = '2'

# p_index = 12
# p_index = 16
p_index = 3

with open(src) as _content:
    contents = _content.readlines()

_contents = [i.strip().replace('"', '') for i in contents]
_contents.pop(0)

for _row in _contents:
    _row = _row.split(';')

    __no_tes = _row[0]
    if __no_tes == '':
        continue

    __pil = _row[p_index]
    if __pil == '':
        continue

    ___pil = __pil.split('.')

    if len(___pil) <= 1:
        continue

    # __pil_dest = dst + __no_tes + '-p'+p+'.' + ___pil[-1]
    __pil_dest = dst + __no_tes + '.' + ___pil[-1]
    if os.path.exists(__pil_dest):
        continue

    try:
        urllib.request.urlretrieve(__pil, __pil_dest)
        print(__pil_dest)
    except:
        print(__pil_dest+' --> file not found!')



    # __pil1 = _row[12]
    # if __pil1 == '':
    #     continue

    # ___pil1 = __pil1.split('.')

    # if len(___pil1) <= 1:
    #     continue

    # __pil1_dest = dst + __no_tes + '-p1.' + ___pil1[-1]
    # if os.path.exists(__pil1_dest):
    #     continue

    # urllib.urlretrieve(__pil1, __pil1_dest)
    # print(__pil1_dest)

    # __pil2 = _row[18]
    # if __pil2 == '':
    #     continue

    # ___pil2 = __pil2.split('.')

    # if len(___pil2) <= 1:
    #     continue

    # __pil2_dest = dst + __no_tes + '-p2.' + ___pil2[-1]
    # if os.path.exists(__pil2_dest):
    #     continue

    # urllib.urlretrieve(__pil2, __pil2_dest)
    # print(__pil2_dest)
