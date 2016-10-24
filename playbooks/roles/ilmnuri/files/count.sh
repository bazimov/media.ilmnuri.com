#!/bin/bash


f=/var/log/nginx/ilmnuri.access.log-$(date +%Y%m%d).gz

total=$(zless "$f" | grep ".mp3" | wc -l)
android=$(zless "$f" | grep ".mp3" | grep -i "android" | wc -l)
ios=$(zless "$f" | grep ".mp3" | grep -i "apple" | wc -l)

echo -e "$(date +%b-%d-%Y),$total,$android,$ios" >> /opt/count.log
cp /opt/count.log /root/backups/count-$(date +%Y%m%d).log
#tac /opt/countrev.log > /opt/count.log
