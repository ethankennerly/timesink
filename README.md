# timesink

Profile relative time spent in files from git commit logs.

## Features

* Example git log with timestamps and files.
* Format files into one line, ignoring directory.

## Not supported

* Time per commit.
* Divide time per file.
* Estimate hours per file.
* Format report as tab-separated values.
* Merge two repos.
* Ignore days with no commits.
* For first commit of the day average time from last 5 commits to that repo.

## Usage

Log git.  An example you can copy and edit is here:  

        bash ethan_word_garden_git_log.sh

Then estimate the time sink:

        python timesink.py ethan_word_garden.git.log

This gets written to tab-separated values file with the extension '.tsv'.

## Walkthrough

The log will be more convenient if each entry is exactly one line.
So I reformat the files into the first line.

        >>> from timesink import *
        >>> log = '''
        ... 2016-07-23 12:26 -0700:::Delete unused classes in UnityToykit.
        ...
        ...  Assets/Animation/Word_begin.anim           | Bin 10348 -> 10348 bytes
        ...  Assets/Animation/Word_complete.anim        | Bin 10392 -> 10392 bytes
        ...  ticsManager.asset => ClusterInputManager.asset} | Bin 4112 -> 4104 bytes
        ...  3 files changed, 622 insertions(+)
        ... '''
        >>> rows = file_stat_table(log)
        >>> rows
        [['2016-07-23 12:26 -0700', 'Delete unused classes in UnityToykit.', 'Word_begin.anim', 'Word_complete.anim']]

Then I sort the table by times and calculate difference in minutes.
If first commit in the session, equal quarter of session boundary.

        >>> time_diff([['2016-07-23 15:52:02 -0700', '', 'b.py'], 
        ...            ['2016-07-23 12:26:39 -0700', '', 'a.py']], 
        ...             6 * 60, 90)
        [['a.py', 90], ['b.py', 205]]

Like Git Hours, if time is over a threshold, assume separate session.
If only commit in the session, set to quarter of session boundary.
Distribute to file times.

        >>> time_diff([['2016-07-23 15:52:02 -0700', '', 'a.py', 'b.py'], 
        ...            ['2016-07-23 12:26:39 -0700', '', 'a.py'], 
        ...            ['2016-07-22 12:26:39 -0700', '', 'b.py'], 
        ...            ['2016-07-21 12:26:39 -0700', '', 'a.py']], 
        ...             6 * 60)
        [['a.py', 90], ['b.py', 90], ['a.py', 90], ['a.py', 103], ['b.py', 103]]

Group by file names.
Sum minutes per file.
Sort largest first.

        >>> rank([['a.py', 90], ['b.py', 90], ['a.py', 90], 
        ...     ['a.py', 103], ['b.py', 103]])
        [['minutes', 'percent', 'file'], [283, 59, 'a.py'], [193, 41, 'b.py']]

## Reference software

The script "git hours" estimates time spent with about 1 hour in first commit in session and dividing by sessions.

<https://github.com/kimmobrunfeldt/git-hours>


Glass polls each 5 minutes.  However, I am hoping to track time after-the-fact, without spending any time during the work for tracking.

<https://kris.cool/2015/09/time-tracking-with-git/>
