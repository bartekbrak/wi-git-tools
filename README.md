# WI git tools
A collection of tools used by repository police.

# Usage

    pip install --user wi-git-tools
    cd ~/workspace/my_project
    prune_branches
    # verify, copy and paste the output
    git_authors
    # talk to the offenders who left old branches behind

# CHANGELOG

### [2015-06-16]
- Join wi-git-authors in.
- Rename to wi-git-tools

### [2015-06-15]
- rewrite to python

### [2014-09-22]
- unite two scripts into one

### [2014-09-04]
- change xargs to while read loop to prevent wrong output on 0 branches


author: bartek.r@webinterpret.com
