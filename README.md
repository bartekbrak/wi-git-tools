# WI Prune branches
List branches that were already merged and can be safely deleted from local
and remote.

# Usage

    pip install --user wi-prune-branches
    cd ~/workspace/my_project
    prune_branches
    # verify, copy and paste the output

# CHANGELOG

### [2015-06-15]
- rewrite to python

### [2014-09-22]
- unite two scripts into one

### [2014-09-04]
- change xargs to while read loop to prevent wrong output on 0 branches


author: bartek.r@webinterpret.com
