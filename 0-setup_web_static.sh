#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create or update the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of directories
sudo chown -hR ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start
exit 0
