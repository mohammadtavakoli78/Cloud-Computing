#!/usr/bin/env python

import sys


both_likes = 0
both_retweets = 0
both_android = 0
both_iphone = 0
both_web = 0

trump_likes = 0
trump_retweets = 0
trump_android = 0
trump_iphone = 0
trump_web = 0

biden_likes = 0
biden_retweets = 0
biden_android = 0
biden_iphone = 0
biden_web = 0


for line in sys.stdin:
    line.strip()
    candidate_name, number_of_likes, number_of_retweets, Web, iPhone, Android = line.split("\t")
    if candidate_name == "Both":
        both_likes += int(float(number_of_likes))
        both_retweets += int(float(number_of_retweets))
        both_android += int(float(Android))
        both_iphone += int(float(iPhone))
        both_web += int(float(Web))
    elif candidate_name == "Trump":
        trump_likes += int(float(number_of_likes))
        trump_retweets += int(float(number_of_retweets))
        trump_android += int(float(Android))
        trump_iphone += int(float(iPhone))
        trump_web += int(float(Web))
    elif candidate_name == "Biden":
        biden_likes += int(float(number_of_likes))
        biden_retweets += int(float(number_of_retweets))
        biden_android += int(float(Android))
        biden_iphone += int(float(iPhone))
        biden_web += int(float(Web))


print("%s %s %s %s %s %s" % ("Both Candidate", both_likes, both_retweets, both_web, both_iphone, both_android))
print("%s %s %s %s %s %s" % ("Trump", trump_likes, trump_retweets, trump_web, trump_iphone, trump_android))
print("%s %s %s %s %s %s" % ("Biden", biden_likes, biden_retweets, biden_web, biden_iphone, biden_android)) 
