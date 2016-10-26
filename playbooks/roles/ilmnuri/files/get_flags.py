#!/usr/bin/python

import gzip
import operator
import memcache
from geoip import geolite2
from datetime import datetime


def flags():
    client = memcache.Client([('127.0.0.1', 11211)])
    dt = datetime.now().strftime('%Y%m%d')

    d = {}
    with gzip.open('/var/log/nginx/access.log-{0}.gz'.format(dt), 'r') as fin:
        for line in fin:
            ip = line.split('-')[0].rstrip()
            match = geolite2.lookup(ip)
            if match is not None:
                c = match.country
                if c in d and c is not None:
                    d[c] += 1
                else:
                    d[c] = 1

    sorted_x = sorted(d.items(), key=operator.itemgetter(1))
    sorted_x.reverse()

    client.set('flags', sorted_x[:20], time=43200)

if __name__ == '__main__':
    flags()
