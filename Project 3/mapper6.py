#!/usr/bin/env python

import sys
import csv
import datetime

STATES_LAT_LONG = {"new york": {"min_long": -79.7624, "max_long": -71.7517, "min_lat": 40.4772, "max_lat": 45.0153},
                   "california": {"min_long": -124.6509, "max_long": -114.1315, "min_lat": 32.5121, "max_lat": 42.0126}}

STATES = ["new york", "california"]


def check_state_lat_long(lat, long):
    if (STATES_LAT_LONG["new york"]["min_long"] < long < STATES_LAT_LONG["new york"]["max_long"]) and (
            STATES_LAT_LONG["new york"]["min_lat"] < lat < STATES_LAT_LONG["new york"]["max_lat"]):

        return True, "new york"

    elif (STATES_LAT_LONG["california"]["min_long"] < long < STATES_LAT_LONG["california"]["max_long"]) and (
            STATES_LAT_LONG["california"]["min_lat"] < lat < STATES_LAT_LONG["california"]["max_lat"]):
        return True, "california"


def check_date_time(created_at):
    [_, time] = created_at.split()
    [hours, minutes, seconds] = time.split(":")

    tweet_time = datetime.time(int(hours), int(minutes), int(seconds))
    if datetime.time(9, 0, 0) <= tweet_time <= datetime.time(17, 0, 0):
        return True

    return False


input_data = csv.reader(sys.stdin)
next(input_data)

for row in input_data:
    try:
        created_at, tweet, lat, long = row[0], row[2], float(row[13]), float(row[14])
        if (tweet.__contains__("#Biden") or tweet.__contains__("#JoeBiden")) and (
                tweet.__contains__("#Trump") or tweet.__contains__("#DonaldTrump")):
            is_state, state = check_state_lat_long(lat, long)

            if check_date_time(created_at) and is_state:
                print(f'{state.lower()}\tBoth')

        elif tweet.__contains__("#Trump") or tweet.__contains__("#DonaldTrump"):
            is_state, state = check_state_lat_long(lat, long)
            if check_date_time(created_at) and is_state:
                print(f'{state.lower()}\tTrump')

        elif tweet.__contains__("#Biden") or tweet.__contains__("#JoeBiden"):
            is_state, state = check_state_lat_long(lat, long)

            if check_date_time(created_at) and is_state:
                print(f'{state.lower()}\tBiden')

    except:
        pass
