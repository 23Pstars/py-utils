#!/usr/bin/python

# fetch beberapa bio namet-namet ayas http://elektro08.com#namets

import urllib2
import json
import sys

api = 'http://api.lrsoft.id/instagram/v1/user'
ig_file = '/Users/zaf/Sites/github/elektro08-web/IG_ACCOUNTS'
namet_dir = '/Users/zaf/Sites/github/elektro08-web/_source/_namets/'

with open(ig_file) as _content:
    contents = _content.readlines()

accounts = [i.strip() for i in contents if i[0] == '@']

for _user in accounts:
    _url = api + '?user=' + _user[1:]
    _response = json.loads(urllib2.urlopen(_url).read())
    _namet = _response['user']

    _namet_file = open(namet_dir + _namet['username'] + '.md', 'w')
    sys.stdout = _namet_file

    print '---'
    print 'nick: ' + _namet['username']
    print 'name: ' + _namet['full_name']
    print 'photo: ' + _namet['profile_pic_url_hd']

    if _namet['external_url'] is not None:
        print 'web: ' + _namet['external_url']

    print '---'
