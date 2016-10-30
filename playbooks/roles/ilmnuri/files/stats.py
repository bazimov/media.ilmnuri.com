#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
from datetime import datetime
import os
import gzip

con = lite.connect('/usr/share/nginx/html/stats.db')

dt = datetime.now().strftime('%Y%m%d')
dt_value = datetime.now().strftime('%b-%d-%Y')
log_file = '/var/log/nginx/access.log-{0}.gz'.format(dt)
count = 0

if os.path.isfile(log_file):
    with gzip.open(log_file, 'r') as f:
        for line in f:
            if "mp3" in line:
                count += 1
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO stats VALUES(?,?);", (dt_value, count))

