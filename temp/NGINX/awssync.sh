#!/bin/bash

/usr/bin/aws s3 sync s3://api.ilmnuri.com/AbuNur/ /usr/share/nginx/html/AbuNur
/usr/bin/aws s3 sync s3://api.ilmnuri.com/Ayyubxon/ /usr/share/nginx/html/Ayyubxon
/usr/bin/aws s3 sync s3://api.ilmnuri.com/Abdulloh/ /usr/share/nginx/html/Abdulloh

echo "job complete $(date)" >> /tmp/awssync.log
