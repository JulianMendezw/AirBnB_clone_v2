#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local, hide
from datetime import datetime
import os


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
