"""
Display information abut commits on remote branches. Useful to detect orphaned
code.
"""

import argparse
import re
from blessings import Terminal
from git import Repo
from git_common import info

repo = Repo()
t = Terminal()

WRONG_BRANCH = re.compile('->|/master|HEAD|/develop')

# It would be much more readable and interesting to not use the git formatting
# but retrieve all data and format in python
format_ = (
    '%C(yellow)%h%x09%C(reset)%ar %C(green bold)'
    '%an%x09%x09%C(reset)%C(bold)%s%C(reset)'
)


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    return parser.parse_args()


def remote_branches_info():
    info('Remote branches:')
    remotes = [
        remote.strip()
        for remote
        in repo.git.branch(remotes=True).split('\n')
        if not WRONG_BRANCH.search(remote)
    ]
    for branch in remotes:
        print(branch)
        print(repo.git.log(
            branch,
            '^origin/master',
            no_merges=True,
            pretty='format:%s' % format_
        ))
        print


def main():
    global args
    args = parse_args()
    info('Working on %s' % repo)
    repo.remotes.origin.fetch(p=True)
    remote_branches_info()

if __name__ == '__main__':
    main()
