# timesink

Profile relative time spent in files from git commit logs.

## Features

* Example git log with timestamps and files.

## Not supported

* Format files into one line, ignoring directory.
* Time per commit.
* Divide time per file.
* Estimate hours per file.
* Format report as tab-separated values.
* Merge two repos.
* Ignore days with no commits.
* For first commit of the day average time from last 5 commits to that repo.

## Reference software

Git hours estimates time spent:

<https://github.com/kimmobrunfeldt/git-hours>

<http://stackoverflow.com/questions/5246344/time-trackinggit-measuring-effort-per-commit>

Glass polls each 5 minutes:

<https://kris.cool/2015/09/time-tracking-with-git/>

## Walkthrough

Log git.  An example you can copy and edit is here:  

        bash git\_log\_ethan.sh

The log will be more convenient if each entry is exactly one line.

So I reformat the files into the first line.

        >>> from timesink import *
        >>> log = '''
        ... 2016-07-23 12:26:::Delete unused classes in UnityToykit.
        ...
        ...  Assets/Animation/Word_begin.anim           | Bin 10348 -> 10348 bytes
        ...  Assets/Animation/Word_complete.anim        | Bin 10392 -> 10392 bytes
        ...  ticsManager.asset => ClusterInputManager.asset} | Bin 4112 -> 4104 bytes
        ...  3 files changed, 622 insertions(+)
        ... '''
        >>> table = file_stat_table(log)
        >>> table
        [['2016-07-23 12:26', 'Delete unused classes in UnityToykit.', 'Word_begin.anim', 'Word_complete.anim']]


