#!/usr/bin/env python

import sys
import string

from datetime import datetime
from dateutil import tz
from datetime import time

table = string.maketrans("","")

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split(',')
    #print '%s' % tokens[0]
    # METHOD 1: Hardcode zones:
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')

    # utc = datetime.utcnow()
    #Wed Aug 27 13:08:45 +0000 2008
    #ts = time.strftime('%Y-%m-%d %H:%M:%S', date(tokens[0]),'%a %b %d %H:%M:%S +0000 %Y')
    try:
        utc = datetime.strptime(tokens[0], '%a %b %d %H:%M:%S +0000 %Y')
        #print '%s' % utc
        # Tell the datetime object that it's in UTC time zone since 
        # datetime objects are 'naive' by default
        utc = utc.replace(tzinfo=from_zone)

        # Convert time zone
        central = utc.astimezone(to_zone)
        print '%s' % central
    except:
        pass
