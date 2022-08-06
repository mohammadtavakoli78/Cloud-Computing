#!/usr/bin/env python

import sys

new_york_total = 0
california_total = 0

president = {
    "Both": {"new york": 0, "california": 0},
    "Trump": {"new york": 0, "california": 0},
    "Biden": {"new york": 0, "california": 0}
}

STATES = ["new york", "california"]

for line in sys.stdin:
    line.strip()
    state, name = line.split("\t")
    name = name.rstrip()

    president[name][state] += 1

for pres in list(president.keys()):
    new_york_total += president[pres]["new york"]
    california_total += president[pres]["california"]

print("%s %s %s %s %s" % (
    "new york", president["Both"]["new york"] / new_york_total, president["Biden"]["new york"] / new_york_total,
    president["Trump"]["new york"] / new_york_total, new_york_total))

print("%s %s %s %s %s" % (
    "california", president["Both"]["california"] / california_total, president["Biden"]["california"] / california_total,
    president["Trump"]["california"] / california_total, california_total))
