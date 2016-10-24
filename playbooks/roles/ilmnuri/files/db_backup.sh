#!/bin/bash

/usr/bin/sqlite3 /usr/share/nginx/html/app/tokens.db .dump > /root/backups/token_db_$(date +"%m_%d_%Y").bak

cd /root/backups/
/usr/bin/aws s3 sync . s3://dbbackup.ilmnuri.com/
