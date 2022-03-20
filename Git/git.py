# import lib
import os


def init(sub_cmd: str = None):
    """
    Initialize empty Git repository
    :param sub_cmd:
    """
    if sub_cmd:
        os.system(f"git init {sub_cmd}")
    os.system("git init")


def add(files: str = ".", sub_cmd: str = None) -> None:
    """
    Add files to the staging area
    :param sub_cmd: subcommand for git add
    :param files: To files add in the staging area, default is '.'
    """
    if sub_cmd:
        os.system(f"git add {sub_cmd}" + files)
    os.system("git add " + files)


def commit(message: str, sub_cmd: str = "-m") -> None:
    """
    Commit changes
    :param sub_cmd: subcommand for git commit like -m, -am and many other
    default is '-m'
    :param message: To store in git history
    :return:
    """
    os.system(f'git commit {sub_cmd} "{message}"')


def status(sub_cmd: str = None) -> None:
    """
    Shows the files in the staging
    :return None:
    """
    if sub_cmd:
        os.system(f"git status {sub_cmd}")
    os.system("git status")


def get_help(command: str = '--help', open_online: bool = False, sub_cmd: str = None) -> None:
    """
    Get help on specific git command
    :param sub_cmd:
    :param open_online: if true, it will open browser else in terminal or command
    :param command: git command to know
    """
    if open_online:
        if not command == "--help":
            if sub_cmd:
                os.system(f"git {command} --help {sub_cmd}")
            os.system(f"git {command} --help")
        if sub_cmd:
            os.system(f"git {command} --help {sub_cmd}")
        os.system(f"git {command}")
    else:
        if not command == "--help":
            if sub_cmd:
                os.system(f"git {command} --help {sub_cmd}")
            os.system(f"git {command} --h")
        if sub_cmd:
            os.system(f"git {command} --help {sub_cmd}")
        os.system(f"git --h")


def branch(branch_name: str = "main", sub_cmd: str = '-M') -> None:
    """
    Create branch
    :param sub_cmd: git branch command like '-M', 'default '-M'
    :param branch_name: name of branch to be created
    :return None:
    """
    os.system(f"git branch {sub_cmd} {branch_name}")


def remote(url: str, cmd: str = "add", sub_cmd: str = "origin") -> None:
    """
    Set the url
    :param url: GitHub url to be push or set
    :param cmd: git remote command for example add, remove, rename and other, default 'add'
    :param sub_cmd: git remote subcommand for example origin, [--push] [--all], default 'origin'
    :return None:
    """
    os.system(f"git remote {cmd} {sub_cmd} {url}")


def push(branch_name: str, cmd: str = "-u", sub_cmd: str = "origin") -> None:
    """
    Push files to GitHub
    :param branch_name: Branch to push to
    :param cmd: git push command like '-u', '-v' and other, default '-u'
    :param sub_cmd: git push subcommand for example 'origin', default 'origin'
    :return None:
    """
    os.system(f"git push {cmd} {sub_cmd} {branch_name}")
