#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy. """
from fabric.api import local, hide, env, run, put
from datetime import datetime
import os
env.user = "ubuntu"
env.hosts = ["35.190.147.175", "54.204.101.31"]


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
    """ Deploy the archive and configure the web server """

    if not os.path.exists(archive_path):
        return(False)
    try:
        put(archive_path, "/tmp/")
        folder_path = "/data/web_static/releases/" + archive_path[9:-4]
        name_file = archive_path[9:]
        name_folder = archive_path[9:-4]
        date = archive_path[21:-4]
        releases = "/data/web_static/releases/"

        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(name_file, folder_path))
        run("rm /tmp/{}".format(name_file))
        run("mv {}{}/web_static/* {}{}/"
            .format(releases, name_folder, releases, name_folder))
        run("rm -rf {}{}/web_static".format(releases, name_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print("New version deployed!")

        return(True)
    except BaseException:
        return (False)


def deploy():
    """ Fabric script (based on the file 2-do_deploy_web_static.py) that
        creates and distributes an archive to your web servers,
        using the function deploy: """

    archive_path = do_pack()

    if not file_path:
        return(False)

    return do_deploy(archive_path)
