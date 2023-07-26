#!/usr/bin/python3
"""
Script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
import subprocess
import os


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.isdir("versions"):
            subprocess.run(["mkdir", "versions"], check=True)
        file_name = "versions/web_static_{}.tgz".format(date)
        subprocess.run(["tar", "-cvzf", file_name, "web_static"], check=True)
        return file_name
    except subprocess.CalledProcessError:
        return None


do_pack()
