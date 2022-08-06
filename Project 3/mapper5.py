#!/usr/bin/env python

import sys
import csv
import datetime


def check_date_time(created_at):
    [_, time] = created_at.split()
    [hours, minutes, seconds] = time.split(":")

    tweet_time = datetime.time(int(hours), int(minutes), int(seconds))
    if datetime.time(9, 0, 0) <= tweet_time <= datetime.time(17, 0, 0):
        return True

    return False


def validate_state(state):
    if state in STATES:
        return True
    return False


STATES = ["new york", "texas", "california", "florida"]

input_data = csv.reader(sys.stdin)
next(input_data)

for row in input_data:
    try:
        created_at, tweet, state = row[0], row[2], row[18]

        if (tweet.__contains__("#Biden") or tweet.__contains__("#JoeBiden")) and (
                tweet.__contains__("#Trump") or tweet.__contains__("#DonaldTrump")):
            if validate_state(state.lower()) and check_date_time(created_at):
                print(f'{state.lower()}\tBoth')

        elif tweet.__contains__("#Trump") or tweet.__contains__("#DonaldTrump"):
            if validate_state(state.lower()) and check_date_time(created_at):
                print(f'{state.lower()}\tTrump')

        elif tweet.__contains__("#Biden") or tweet.__contains__("#JoeBiden"):
            if validate_state(state.lower()) and check_date_time(created_at):
                print(f'{state.lower()}\tBiden')

    except:
        pass
