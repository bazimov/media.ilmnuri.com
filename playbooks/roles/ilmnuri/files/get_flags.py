#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import gzip
import sqlite3 as lite
from glob import glob
from geoip import geolite2
from datetime import datetime


def flags():
    con = lite.connect('/usr/share/nginx/html/flags.db')
    dt = datetime.now().strftime('%Y%m%d')

    d = {}
    with gzip.open('/var/log/nginx/access.log-{0}.gz'.format(dt), 'r') as fin:
        for line in fin:
            if "mp3" in line:
                ip = line.split('-')[0].rstrip()
                match = geolite2.lookup(ip)
                if match is not None:
                    c = match.country
                    if c in d and c:
                        d[c] += 1
                    else:
                        d[c] = 1

    with con:
        cur = con.cursor()
        os.chdir('/usr/share/nginx/html/app/static/flags/')
        countries = sorted(glob('*'))
        for k, v in d.items():
            key = countries.index('{0}.png'.format(k)) + 1
            cur.execute('select total from flags where id = {0};'.format(key))
            t = cur.fetchone()
            total = v + t[0]
            cur.execute('update flags set today = {0},total = {1} '
                        'where id = {2};'.format(v, total, key))

if __name__ == '__main__':
    flags()
