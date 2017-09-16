import argparse
import os.path

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from googleplaces import GooglePlaces, types, lang

def is_valid_file(parser, arg):
    ''' check if file is valid '''
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r') #return open file

def read_to_dict(open_file):
    ''' read from file format to dictionary ''' 
    lines = open_file.readlines()
    ret_dict = {}
    for line in lines:
        ret_dict[line.split(': ')[0]] = line.split(': ')[1]
    return ret_dict

def parse_args():
    ''' parse bash args, confusingly named '''
    parser = argparse.ArgumentParser(description="recommender for tailorfood")
    parser.add_argument("--num", dest="number",
        help="number of results to return",
        default=1, type=int, required=False)
    parser.add_argument("--radius", dest="radius",
        help="radius given by user",
        default=10, type=int, required=False)
    parser.add_argument("-l", dest="location",
        help="location of user",
        type=str, required=True)

    parser.add_argument("-r", dest="restaurant_path",
        help="restaurants database filepath", metavar="FILE", required=True,
        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-c", dest="cuisine_path",
        help="cuisines database filepath", metavar="FILE", required=True,
        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-k", dest="key_path",
        help="keyfile filepath", metavar="FILE", required=True,
        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()

    return {
        num: args.number,
        radius: args.radius,
        location: args.location,
        restaurants: [line.strip() for line in args.restaurant_path],
        cuisines: [line.strip() for line in args.cuisine_path],
        keys: read_to_dict(args.key_path)
    }


def recommend(yelp_auth, google_places):
    ''' 
        return reccomendation:
         - if result is already in their favourites, reccomend another
    '''
    return []

if __name__ == "__main__":
    args = parse_args()
    yelp_auth = Oauth1Authenticator(
        consumer_key=args.keys.YELP_KEY,
        consumer_secret=args.keys.YELP_SECRET,
        token=args.keys.YELP_TOKEN,
        token_secret=args.keys.YELP_TOKEN_SECRET
    )
    google_places = GooglePlaces(args.keys.GOOGLE_KEY)

    print("starting tailorfood reccomender engine...")
    for x in recommend(yelp_auth, google_places, args): print(x)
    print("closing.")

