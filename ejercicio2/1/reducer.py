#!/usr/bin/env python


### Nota: el framework de hadoop garantiza que todos los
###  valores asociados con la misma clave (palabra) van al mismo reducer

from operator import itemgetter #No lo esta usando
import sys

current_user = None
current_count = 0
user = None
max_user = None
max_count = 0
first_execution = True

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    user, count = line.split('\t', 1)

    
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    if first_execution:
        max_user = user
        max_count = count
        first_execution = False

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: user) before it is passed to the reducer
    if current_user == user:
        current_count += count
        # It is checked if after the increment the user has the most accesess
        if current_count >= max_count:
            max_user = user
            max_count = current_count
    else:
        current_count = count
        current_user = user
print '%s\t%s' % (max_user, max_count)