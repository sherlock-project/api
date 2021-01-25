"""Helper and Utility module.
"""
import os
import json

def py_command():
    """Return valid Python executable command base on current OS."""
    return "python" if os.name == 'nt' else "python3"

def cmd_in_dir(newdir, cmd):
    """Preserve current working directory and execute command
    in new directory.

    Keyword Arguments:
    newdir -- Target directory to navigate to.
    cmd    -- Command you would like to execute.
    """
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        print(os.getcwd())
        os.system(cmd)
    finally:
        os.chdir(prevdir)

# Security

def valid_args(cmd):
    """Return true, if command is safe to execute."""
    escape = [";", "&", "|", "<", ">" "\"" "\'"]
    for ch in escape:
        if ch in cmd:
            return False
    return True


# Sherlock Related

def sherlock_dir():
    """Return sherlock project root directory."""
    return "./execution/sherlock"

def sherlock_data():
    """Return `data.json` file from sherlock project."""
    data_path = f"{sherlock_dir()}/sherlock/resources/data.json"
    with open(data_path, "r", encoding="utf-8") as data_file:
        data = json.load(data_file)
    return data
