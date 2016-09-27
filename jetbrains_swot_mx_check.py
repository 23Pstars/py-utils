#!/usr/bin/python

# https://github.com/JetBrains/swot/pull/2325

import os
from subprocess import call

domains_dir = '/Users/zaf/Downloads/swot/lib/domains/id/ac'
updated_domains_dir = '/Users/zaf/Sites/github/swot/lib/domains/id/ac'

updated_files = os.listdir(updated_domains_dir)
for univ_file in os.listdir(domains_dir):
    if univ_file not in updated_files:
        univ_site = os.path.splitext(univ_file)[0] + '.' + os.path.basename(domains_dir) + '.' + os.path.basename(
            os.path.dirname(domains_dir))
        call('host -t mx ' + univ_site, shell=True)
        print '=============================\n'
