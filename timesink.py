#!/bin/python
"""
Usage: 
    Change to this directory. 
    Create git log.
        Example: bash ethan_word_garden_git_log.sh
    python timesink.py ethan_word_garden.git.log
    Details in README.md
"""

from csv import writer
from datetime import datetime
from math import ceil

delimiter = '\t'


def file_stat_table(log):
    lines = log.splitlines()
    trimmed_lines = []
    files = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        elif ' ' == line[0]:
            if ' files changed' in line or ' file changed' in line:
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


def time_diff(table, session_minutes_max = 60 * 6, minutes_default = 90):
    rows = []
    table.sort()
    date_previously = None
    minutes_default = session_minutes_max / 4
    for original_row in table:
        timestamp = original_row[0]
        parts = timestamp.split(' ')
        no_time_zone = ' '.join(parts[:2])
        date = datetime.strptime(no_time_zone, '%Y-%m-%d %H:%M:%S')
        if date_previously:
            delta = date - date_previously
            minutes = int(round(delta.total_seconds() / 60.0))
            if session_minutes_max < minutes:
                minutes = minutes_default
        else:
            date_previously = date
            minutes = minutes_default
        shares = original_row[2:]
        if shares:
            per = int(ceil(minutes / float(len(shares))))
            for share in shares:
                row = [share, per]
                rows.append(row)
            date_previously = date
    return rows


def rank(name_minutes):
    totals = {}
    for name, minute in name_minutes:
        if not name in totals:
            totals[name] = 0
        totals[name] += minute
    ranks = []
    denominator = 0
    for total in totals.values():
        denominator += total
    for name, total in totals.items():
        percent = int(round(100.0 * total / denominator))
        ranks.append([total, percent, name])
    ranks.sort(reverse=True)
    ranks.insert(0, ['minutes', 'percent', 'file'])
    return ranks


def write_tsv(path, table):
    """
    http://stackoverflow.com/questions/14780702/how-to-read-and-write-a-table-matrix-to-file-with-python
    """
    with open(path, 'w') as csvfile:
        write = writer(csvfile, delimiter=delimiter)
        [write.writerow(r) for r in table]


def profile_log_file(filepath):
    log = open(filepath).read()
    table = file_stat_table(log)
    name_minutes = time_diff(table)
    ranks = rank(name_minutes)
    out = filepath + '.tsv'
    write_tsv(out, ranks)
    return out


if '__main__' == __name__:
    from sys import argv
    if 2 <= len(argv):
        print(profile_log_file(argv[1]))
    else:
        print(__doc__)
    from doctest import testfile
    testfile('README.md')
