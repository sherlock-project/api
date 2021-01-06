#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from os import path
import sys

from helper import *

def init_sherlock():
    """Get the newest Sherlock project."""
    print("[INFO] Prepare for Sherlock Project..")
    if path.exists(sherlock_dir()):
        cmd_in_dir(sherlock_dir(), f"git pull")  # Update to the newest version
    else:  # Othersie, clone it once
        os.system(f"git clone https://github.com/sherlock-project/sherlock {sherlock_dir()}");
    os.system(f"{py_command()} -m pip install -r {sherlock_dir()}/requirements.txt")
    os.system(f"{py_command()} {sherlock_dir()}/sherlock --version")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    init_sherlock()
    main()
