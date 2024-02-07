#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test 
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data

# Create a fake HTML file
echo "<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <p>This is a test page for web_static deployment.</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or update the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_block="location /hbnb_static { 
  alias /data/web_static/current/;
  index index.html;
  }
  "
sudo sed -i "/server {/a $config_block" /etc/nginx/sites-available/default}

# Restart Nginx
sudo service nginx restart
exit 0
