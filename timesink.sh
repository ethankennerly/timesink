#!/bin/bash

# Usage:  bash timesink.sh git_repo_directory author_name

wd=`pwd`
dir=$1
author=$2
log=$wd/$author.timesink.git.log

cd $dir
git log --format="%cd:::%s" --author $author --date=iso --stat > $log
cd $wd
python timesink.py $log
