#!/bin/bash

dt=$(date +"%m_%d_%Y")
/usr/bin/sqlite3 /usr/share/nginx/html/app/tokens.db .dump > /root/backups/token_db_"$dt".bak
/usr/bin/sqlite3 /usr/share/nginx/html/stats.db .dump > /root/backups/stats_db_"$dt".bak
/usr/bin/sqlite3 /usr/share/nginx/html/flags.db .dump > /root/backups/flags_db_"$dt".bak

cd /root/backups/
/usr/bin/aws s3 sync . s3://dbbackup.ilmnuri.com/
