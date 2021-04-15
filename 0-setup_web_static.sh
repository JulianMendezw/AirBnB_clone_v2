#!/usr/bin/env bash
# el comentario
sudo apt-get update -y
sudo apt install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "HI Holberton" > /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

HOLA="\\\tlocation /hbnb_static/ \{\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}"

sed -i "49i $HOLA" /etc/nginx/sites-available/default

sudo service nginx restart
