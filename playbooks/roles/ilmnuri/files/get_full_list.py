#!/usr/bin/python
# -*- coding: utf-8 -*-

import memcache
from glob import glob
import os


def main():
    os.chdir('/usr/share/nginx/html/')
    client = memcache.Client([('127.0.0.1', 11211)])

    list_items = glob('Abdulloh/*/*') + glob('AbuNur/*/*') + glob('Ayyubxon/*/*')
    dictionary = {'Abdulloh': {}, 'AbuNur': {}, 'Ayyubxon': {}}

    for item in list_items:
        s = item.split('/')
        if s[1] not in dictionary[s[0]]:
            dictionary[s[0]][s[1]] = []

    for item in list_items:
        s = item.split('/')
        if s[1] in dictionary[s[0]].keys():
            if s[2]:
                dictionary[s[0]][s[1]].append(s[2])
    dictionary['Abdulloh']['0_Appni_yangi_versiyasiga_yangilang'] = [
        'Bu_appni_versiyasi_eski.mp3',
        'iltimos_yangilab_oling.mp3',
        'Play_marketda_oxirgi_3.3_verisya_bor.mp3',
        'Yaqinda_bu_versiya_ishlamay_qolishi_mumkin.mp3']
    dictionary['Abdulloh'].pop('1_Yangi_Ramazon_2016', None)

    client.set('album', dictionary, time=43200)


def new_api():
    os.chdir('/usr/share/nginx/html/')
    client = memcache.Client([('127.0.0.1', 11211)])

    list_items = glob('Abdulloh/*/*') + glob('AbuNur/*/*') + glob('Ayyubxon/*/*')
    dictionary = {'Abdulloh': {}, 'AbuNur': {}, 'Ayyubxon': {}}

    for item in list_items:
        s = item.split('/')
        if s[1] not in dictionary[s[0]]:
            dictionary[s[0]][s[1]] = []

    for item in list_items:
        sz = '{0} MB'.format(os.path.getsize(item) / 1024000)
        s = item.split('/')
        if s[1] in dictionary[s[0]].keys():
            if s[2]:
                dictionary[s[0]][s[1]].append((s[2], sz))

    client.set('album2', dictionary, time=43200)


if __name__ == '__main__':
    main()
    new_api()