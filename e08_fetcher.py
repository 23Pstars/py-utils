#!/usr/bin/python

# fetch beberapa bio namet-namet ayas http://elektro08.com#namets

import urllib
import json
import sys

api = 'https://api.lrsoft.id/instagram/v1/user'
ig_file = '/Users/zaf/Sites/github/elektro08-web/IG_ACCOUNTS'
namet_file_dir = '/Users/zaf/Sites/github/elektro08-web/_source/_namets/'
uri_namet_img_dir = '/assets/img/namets/'
abs_namet_img_dir = '/Users/zaf/Sites/github/elektro08-web/_source/assets/img/namets/'

with open(ig_file) as _content:
    contents = _content.readlines()

accounts = [i.strip() for i in contents if i[0] == '@']

for _user in accounts:
    _url = api + '?user=' + _user[1:]
    _response = json.loads(urllib.urlopen(_url).read())
    _namet = _response['user']

    _nick = _namet['username']
    _ig_profile_pic = _namet['profile_pic_url_hd']
    _profile_pic = _nick + '.' + _ig_profile_pic.rsplit('.', 1)[1]

    urllib.urlretrieve(_ig_profile_pic, abs_namet_img_dir + _profile_pic)

    _namet_file = open(namet_file_dir + _namet['username'] + '.md', 'w')
    sys.stdout = _namet_file

    print '---'
    print 'nick: ' + _namet['username']
    print 'name: ' + _namet['full_name']
    print 'photo: ' + uri_namet_img_dir + _profile_pic

    if _namet['external_url'] is not None:
        print 'web: ' + _namet['external_url']

    print '---'
