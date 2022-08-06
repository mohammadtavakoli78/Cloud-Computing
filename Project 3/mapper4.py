#!/usr/bin/env python

import sys
import csv


def define_social_media_type(device):
    iPhone, Android, Web = 0, 0, 0
    if device.__contains__("iPhone"):
        iPhone = 1
    elif device.__contains__("Android"):
        Android = 1
    elif device.__contains__("Web"):
        Web = 1

    return f'{Web}\t {iPhone}\t {Android}'


input_data = csv.reader(sys.stdin)
next(input_data)

for row in input_data:
    try:
        tweets_text, number_of_like, number_of_retweets, device_type = row[2], row[3], row[4], row[5]
        if (tweets_text.__contains__("#Biden") or tweets_text.__contains__("#JoeBiden")) and (
                tweets_text.__contains__("#Trump") or tweets_text.__contains__("#DonaldTrump")):
            print(f'Both\t {number_of_like}\t {number_of_retweets}\t {define_social_media_type(device_type)}')

        elif tweets_text.__contains__("#Trump") or tweets_text.__contains__("#DonaldTrump"):
            print(f'Trump\t {number_of_like}\t {number_of_retweets}\t {define_social_media_type(device_type)}')

        elif tweets_text.__contains__("#Biden") or tweets_text.__contains__("#JoeBiden"):
            print(f'Biden\t {number_of_like}\t {number_of_retweets}\t {define_social_media_type(device_type)}')

    except:
        pass
