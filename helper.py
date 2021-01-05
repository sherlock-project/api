"""Helper and Utility module.
"""
import os

def py_command():
    """Return valid Python executable command base on current OS."""
    return "python" if os.name == 'nt' else "python3"

def sherlock_dir():
    """Return sherlock project root directory."""
    return "./execution/sherlock"

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
