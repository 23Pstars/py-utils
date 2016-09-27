#!/usr/bin/python

# buat verify web-web universitas di indonesia  dalam program free student subscription di Jetbrains

import os
import time
import bs4
import urllib

delay_offset = 20
delay_interval = 30
search_engine_url = 'http://duckduckgo.com/html'
domains_dir = '/Users/zaf/Sites/github/swot/lib/domains/id/ac'

iteration = 0
for univ_file in os.listdir(domains_dir):
    iteration += 1
    univ_name = open(domains_dir + '/' + univ_file).readline()
    site = urllib.urlopen(search_engine_url + '?q=' + urllib.quote_plus(univ_name))
    parsed = bs4.BeautifulSoup(site.read(), "html.parser")
    url_result = parsed.find('a', {'class': 'result__a'})
    if url_result is None:
        url = 'No results'
    else:
        url = url_result.get('href')
    print univ_file + ' --> ' + url + ' (' + univ_name.rstrip() + ')'
    if iteration == delay_offset:
        print 'Delaying...'
        iteration = 0
        time.sleep(delay_interval)
