#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime
import os
import shutil


def do_pack():

    source_folder = "web_static"
    name_file = (source_folder +
                 datetime.now().strftime('%Y%m%d%H%M%S') + ".tgz")
    path = "/versions"

    print("Packing web_static to versions/" + name_file)

    local("tar -cvzf {} {} && chmod 664 {}"
          .format(name_file, source_folder, name_file))

    try:
        os.mkdir("versions")
    except FileExistsError:
        pass

    size = str(os.path.getsize(name_file))
    print("web_static packed: versions/" + name_file + " -> " + size + "Bytes")

    shutil.move("./{}".format(name_file), ".{}/{}".format(path, name_file))

    if os.path.isfile("{}/{}".format(path, name_file)):
        return "{}/{}".format(path, name_file)

    return None
