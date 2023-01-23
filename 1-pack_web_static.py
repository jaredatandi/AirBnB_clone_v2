#!/usr/bin/python3
"""Fab script"""
import os
from datetime import datetime
from fabric.api import local
try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


def do_pack():
    """Packs web_static into tgz"""
      try:
        # Create versions folder if it doesn't exist
        local("mkdir -p versions")

        # Get current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create archive with current timestamp
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -zcvf versions/{} web_static/".format(archive_name))
        return "versions/{}".format(archive_name)
    except:
        return None
