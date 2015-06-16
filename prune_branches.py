"""
Git wrapper to list remote and local branches that have been merged to master
and can be safely deleted.
"""

import argparse
import re
from blessings import Terminal
from git import Repo
from git_common import info

repo = Repo()
t = Terminal()

WRONG_BRANCH = re.compile('.*(develop|master)$')


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    return parser.parse_args()



def validate_repository_state():
    assert not repo.is_dirty(), 'Dirty status, aborting.'
    assert repo.active_branch.name == 'master', \
        'You need to be on master to do that.'


def prune_remote():
    info('Remote branches:')
    remote_to_prune = [
        remote.strip().replace('origin/', '')
        for remote
        in repo.git.branch(r=True, merged=True).split('\n')
        if not WRONG_BRANCH.match(remote)
    ]
    for branch in remote_to_prune:
        print "{t.blue}git push --delete origin {branch}{t.normal}".format(
            branch=branch, t=t
        )


def prune_local():
    info('Local branches:')
    local_to_prune = [
        local.strip()
        for local
        in repo.git.branch(merged=True).split('\n')
        if not WRONG_BRANCH.match(local)
    ]
    for branch in local_to_prune:
        print "{t.yellow}git branch --delete {branch}{t.normal}".format(
            branch=branch, t=t
        )


def main():
    global args
    args = parse_args()
    validate_repository_state()
    info('Working on %s' % repo)
    repo.remotes.origin.fetch(p=True)
    repo.remotes.origin.pull()
    prune_remote()
    prune_local()

if __name__ == '__main__':
    main()
