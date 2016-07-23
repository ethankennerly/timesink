#!/bin/python
"""
Usage: 
    Change to this directory. 
    Create git log.
        Example: bash git\_log\_ethan.sh
    python timesink.py git.log
"""

separator = '\t'


def file_stat_table(log):
    lines = log.splitlines()
    trimmed_lines = []
    files = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        elif ' ' == line[0]:
            if ' insertions(+)' in line or ' insertion(+)' in line:
                continue
            elif '=>' in line:
                continue
            trim_directory = line.split('/')[-1]
            trim_change = trim_directory.split('|')[0]
            trimmed_file = trim_change.strip()
            files.append(trimmed_file)
        else:
            if files:
                trimmed_lines[-1] += files
            files = []
            row = line.split(':::')
            trimmed_lines.append(row)
    trimmed_lines[-1] += files
    return trimmed_lines


def profile_log_file(filepath):
    log = open(filepath).read()
    return file_stat_table(log)


if '__main__' == __name__:
    from sys import argv
    if 2 <= len(argv):
        print(profile_log_file(argv[1]))
    else:
        print(__doc__)
    from doctest import testfile
    testfile('README.md')
