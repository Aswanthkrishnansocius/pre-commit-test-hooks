from __future__ import annotations

import os.path
import git
from git import Repo
from git import Git

def check_remote(mis_match):
    directory = os.getcwd()
    repo = Repo(directory)
    g = git.cmd.Git()
    print(g.ls_remote('origin').split('\n'))
    print(g.ls_remote('upstream').split('\n'))
    return mis_match   
    
def check_up_to_date(mis_match):
    
    directory = os.getcwd()
    repo = Repo(directory)
    for data in repo.remote().fetch("--dry-run"):
        if data.flags != 4 and (data.remote_ref_path).strip() == "main":
            mis_match = True
            print(
                    f'[FD813].'
                    f'Your local repository is not up'
                    f'to date with production repository'
                )
    if repo.git.rev_list("..remotes/origin/main"):
        mis_match = True
        print(
                    f'[FD813].'
                    f'Your branch is not up to date with origin/13.0'
                )
    return mis_match


def main():
    mis_match = False
    mis_match = check_remote(mis_match)
    mis_match = check_up_to_date(mis_match)
    return True
