#!/bin/bash

# Usage:  bash timesink.sh git_repo_directory

wd=`pwd`
cd $1
git log --format="%cd:::%s" --date=iso --stat > $wd/timesink.git.log
cd $wd
python timesink.py $wd/timesink.git.log
