#!/usr/bin/python

from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostname = raw_input('Hostname: ')
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    s.login(hostname, username, password)
    s.sendline('uptime')
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed to login.")
    print(e)
