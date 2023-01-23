#!/usr/bin/env bash
# setup for deployment
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

SRC="/etc/nginx/sites-available/default"
STATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static_current/;\n\t}\n"
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir "/data/web_static/shared/"
echo "Hello World" | sudo tee "/data/web_static/releases/test/index.html"

if [ -L /data/web_static/current ]; then
  rm -f /data/web_static/current
fi

sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu "/data/"

echo "server {
  listen 80;
  server_name jaredatandi.tech;

  location /hbnb_static {
    alias /data/web_static/current/;
  }
}" > /etc/nginx/sites-available/hbnb_static
ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/

sudo service nginx restart
