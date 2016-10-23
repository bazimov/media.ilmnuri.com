#!/usr/bin/python

import memcache
from geoip import geolite2
import gzip
from glob import glob


def main():
    client = memcache.Client([('127.0.0.1', 11211)])
    full_list = []
    with open('/var/log/nginx/access.log') as f:
        for i in f.readlines():
            ip = i.split('-')[0].strip()
            try:
                place = geolite2.lookup(ip).location
            except:
                place = None
            full_list.append(place)

    print full_list
    #client.set('location', full_list)
    return True

if __name__ == '__main__':
    main()
