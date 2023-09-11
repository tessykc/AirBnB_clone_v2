#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function
do_deploy
"""

from fabric.api import *
import os

env.hosts = ['54.89.117.155', '34.229.137.26']
"""env.user = 'ubuntu'
env.key_filename = '/home/deepanon/.ssh/id_rsa'"""


def do_deploy(archive_path):
    """
    distibute archive to web server and deploy
    """
    if not os.path.exists(archive_path):
        return False
    archive_name = os.path.basename(archive_path)
    archive_no_ext = archive_name.replace('.tgz', '')

    try:
        """upload to /tmp/ on server"""
        put(archive_path, '/tmp/{}'.format(archive_name), use_sudo=True)

        """create release dir"""
        run('mkdir -p /data/web_static/releases/{}'
            .format(archive_no_ext))

        """decompress archive into release dir"""
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(archive_name, archive_no_ext))

        """del archive from server"""
        run('rm /tmp/{}'.format(archive_name))

        run('mv /data/web_static/releases/{}/web_static/*'
            '/data/web_static/releases/{}/'
            .format(archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_no_ext))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
