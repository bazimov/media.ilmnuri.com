#!/bin/bash
# 04.27.2016
# This is to run when newly created cloud vm

yum install epel-release -y
yum update -y
yum install python-devel gcc nginx git python-pip nc -y

git clone https://github.com/bazimov/media.ilmnuri.com.git
pip install uwsgi awscli flask
systemctl disable httpd && systemctl stop httpd
systemctl enable nginx && systemctl start nginx
cp media.ilmnuri.com/NGINX/nginx.conf /etc/nginx/
cp media.ilmnuri.com/service/ilmnuri.service /etc/systemd/system/
cp -r media.ilmnuri.com/* /usr/share/nginx/html/
systemctl enable ilmnuri && systemctl start ilmnuri

chown nginx:nginx -R /usr/share/nginx/html
mkdir -p /usr/share/nginx/html/Abdulloh /usr/share/nginx/html/Ayyubxon /usr/share/nginx/html/AbuNur
systemctl restart ilmnuri && systemctl restart nginx
cp media.ilmnuri.com/NGINX/awssync.sh /opt/
systemctl enable firewalld
systemctl restart firewalld
sudo firewall-cmd --permanent --zone=public --add-service=http 
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --permanent --zone=public --add-service=ssh
sudo firewall-cmd --reload
echo "now configure aws command line with aws config command then run the script /opt/awssync.sh
