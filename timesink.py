#!/bin/python
"""
Usage: 
    Change to this directory. 
    Create git log.
        Example: bash git\_log\_ethan.sh
    python timesink.py git.log
"""

from datetime import datetime

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


def time_diff(table, session_minutes_max = 60 * 6):
    rows = []
    table.sort()
    date_previously = None
    for original_row in table:
        timestamp = original_row[0]
        parts = timestamp.split(' ')
        no_time_zone = ' '.join(parts[:2])
        date = datetime.strptime(no_time_zone, '%Y-%m-%d %H:%M:%S')
        if date_previously:
            delta = date - date_previously
            minutes = int(round(delta.total_seconds() / 60.0))
        else:
            date_previously = date
            minutes = session_minutes_max / 4
        row = [minutes]
        row.extend(original_row[2:])
        rows.append(row)
        date_previously = date
    return rows


def profile_log_file(filepath):
    log = open(filepath).read()
    table = file_stat_table(log)
    return time_diff(table)


if '__main__' == __name__:
    from sys import argv
    if 2 <= len(argv):
        print(profile_log_file(argv[1]))
    else:
        print(__doc__)
    from doctest import testfile
    testfile('README.md')
