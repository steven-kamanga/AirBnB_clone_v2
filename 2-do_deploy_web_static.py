#!/usr/bin/python3

from fabric import env, put, run
from os.path import exists
import os

# Update the IP addresses of your web servers here
env.hosts = ['54.160.115.35", "54.159.2.86']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Get the base filename of the archive without extension
        archive_filename = os.path.basename(archive_path).split('.')[0]

        # Uncompress the archive to /data/web_static/releases/<archive filename without extension> on the web server
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_filename))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(archive_filename, archive_filename))
        run('rm /tmp/{}.tgz'.format(archive_filename))

        # Move the contents of the uncompressed folder to its parent directory
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(archive_filename, archive_filename))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current linked to the new version
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_filename))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", e)
        return False
