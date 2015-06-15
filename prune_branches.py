"""
Git wrapper to list remote and local branches that have been merged to master
and can be safely deleted.
"""

import argparse
import re
import sys
from functools import partial

import pkg_resources
from blessings import Terminal
from git import Repo

repo = Repo()
t = Terminal()

WRONG_BRANCH = re.compile('.*(develop|master)$')


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    # parser.add_argument(
    #     '-n',
    #     '--dry-run',
    #     action='store_true'
    # )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='Print version and exit.'
    )
    return parser.parse_args()


def pprint(msg, level):
    if level == 'info':
        print('# [{t.yellow}INFO{t.normal}] {msg}'.format(msg=msg, t=t))
    elif level == 'called':
        print('# [{t.bold_red}CALLED{t.normal}] {msg}'.format(msg=msg, t=t))

info = partial(pprint, level='info')
called = partial(pprint, level='called')


def validate_repository_state():
    assert not repo.is_dirty(), 'Dirty status, aborting.'
    assert repo.active_branch.name == 'master', \
        'You need to be on master to do that.'


def print_version_and_exit():
    print 'wi-prune-branches', pkg_resources.get_distribution(
        'wi-prune-branches').version,
    print 'from', __file__
    sys.exit()


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
    if args.version:
        print_version_and_exit()
    validate_repository_state()
    info('Working on %s' % repo)
    repo.remotes.origin.fetch()
    repo.remotes.origin.pull()
    prune_remote()
    prune_local()

if __name__ == '__main__':
    main()
