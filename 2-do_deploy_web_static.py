#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function
do_deploy
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.174.92.204', '54.172.150.212']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """
    distibute archive to web server and deploy
    """
    if exists(archive_path) is False:
        return False
    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/<archive filename without extension>
        archive_filename = archive_path.split('/')[-1]
        folder_name = archive_filename.split('.')[0]
        release_path = f'/data/web_static/releases/{folder_name}'
        run(f'mkdir -p {release_path} && tar -xzf /tmp/{archive_filename} -C {release_path}')

        # Delete the uploaded archive from the web server
        run(f'rm /tmp/{archive_filename}')

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version
        run(f'ln -s {release_path} /data/web_static/current')

        print("New version deployed successfully!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
    except:
        return False
