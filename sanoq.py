#!/usr/bin/python

import memcache
from geoip import geolite2
import gzip
from glob import glob
import time


def main():
    client = memcache.Client([('127.0.0.1', 11211)])

    for files in glob('/var/log/nginx/access*'):
        d = {'overall': 0, 'android': 0, 'apple': 0}

        if files.endswith('.gz'):
            cache_key = files.split('-')[1].split('.')[0]
            with gzip.open(files) as f:
                for i in f.readlines():
                    d['overall'] += 1
                    ip = i.split('-')[0].strip()
                    try:
                        place = geolite2.lookup(ip).country
                    except:
                        place = 'None'
                    if place in d.keys():
                        d[place] += 1
                    else:
                        d[place] = 1
                    if 'android' in i.lower():
                        d['android'] += 1
                    elif 'apple' in i.lower():
                        d['apple'] += 1
        else:
            cache_key = time.strftime("%Y%m%d")
            with open(files) as f:
                for i in f.readlines():
                    d['overall'] += 1
                    ip = i.split('-')[0].strip()
                    try:
                        place = geolite2.lookup(ip).country
                    except:
                        place = 'None'
                    if place in d.keys():
                        d[place] += 1
                    else:
                        d[place] = 1
                    if 'android' in i.lower():
                        d['android'] += 1
                    elif 'apple' in i.lower():
                        d['apple'] += 1

        client.set(cache_key, d)


    return True

if __name__ == '__main__':
    main()
