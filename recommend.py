#!/usr/bin/env python3

import argparse
import os.path
import json

def is_valid_file(parser, arg):
    ''' check if file is valid '''
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r') #return open file

def username_matches(users, username):
    ''' return a dictionary in a list that matches usernames '''
    for x in users:
        if x["username"] == username:
            return x

def parse_args():
    ''' parse bash args, confusingly named '''
    parser = argparse.ArgumentParser(description="recommender for tailorfood")
    parser.add_argument("-n", dest="number",
        help="number of results to return",
        default=1, type=int, required=False)
    parser.add_argument("-u", dest="username",
        help="username to recommend for from data.json", required=True,
        type=str)
    parser.add_argument("-f", dest="data_path",
        help="data filepath", metavar="JSON", required=True,
        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    data = json.load(args.data_path)
    user = username_matches(data["users"], args.username)

    return {
        "number": args.number,
        "radius": user["radius"],
        "location": user["location"],
        "restaurants": user["restaurants"],
        "cuisines": user["cuisines"],
        "keys": data["keys"]
    }

def recommend(args):
    ''' 
        return reccomendation:
         - if result is already in their favourites, reccomend another
    '''

    return args["restaurants"]

if __name__ == "__main__":
    args = parse_args()

    print("starting tailorfood reccomender engine...\n")
    for x in recommend(args): print(x)
    print("\nclosing.")

