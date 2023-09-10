#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive web_static
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    compress file
    """
    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None


if __name__ == "__main__":
    archive_path = do_pack()
    if archive_path:
        print("web_static packed: {}".format(archive_path))
    else:
        print("Packaging failed.")
