#!/bin/bash

wd=`pwd`
cd ../flash-unity-port-example
git log --author ethan --format="%cd:::%s" --date=iso --stat > $wd/ethan_word_garden.git.log
cd Assets/Scripts/UnityToyKit
git log --author ethan --format="%cd:::%s" --date=iso --stat >> $wd/ethan_word_garden.git.log
cd $wd
python timesink.py ethan_word_garden.git.log
