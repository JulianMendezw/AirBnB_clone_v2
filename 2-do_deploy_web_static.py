#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy. """
from fabric.api import local, hide, env, run, put
from datetime import datetime
import os
env.user = "ubuntu"
env.hosts = ["35.190.147.175"]


def do_pack():
    """ Function to convert a .tgz archive """

    try:
        source_folder = "web_static"
        name_file = ("web_static" + "_" +
                     datetime.now().strftime('%Y%m%d%H%M%S') + ".tgz")
        path = "/versions"

        print("Packing web_static to versions/" + name_file)

        with hide('running', 'stdout'):
            local("mkdir -p versions")

        local("tar -cvzf versions/{} {}"
              .format(name_file, source_folder))

        with hide('running', 'stdout'):
            size = local("wc -c /etc/passwd | awk '{print $1}'", capture=True)

        print("web_static packed: versions/" +
              name_file + " -> " + size + "Bytes")

        return "{}/{}".format(path, name_file)

    except BaseException:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to  your web serves """

    try:
        # Upload
        put(archive_path, '/tmp/')
        # Uncompress
        dir_name = archive_path[9:-4]
        run('mkdir -p /data/web_static/releases/{}/'.format(dir_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.
            format(dir_name, dir_name))
        #Delete the archive
        run('rm /tmp/{}.tgz'.format(dir_name))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.
            format(dir_name, dir_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.
            format(dir_name))
        #Delete the symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new the symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(dir_name))
    except:
        return False
