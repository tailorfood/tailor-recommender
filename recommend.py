#!/usr/bin/env python3

import argparse
import os.path
import json

import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds


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


# just gets the top n recommendations
def recommend_food(predictions, uID, rID, original_ratings, num_recommendations, restaurants):
    
    # Get and sort the user's predictions
    user_row_number = uID - 1 # user starts at 1, not 0
    # not EXACTLY sure how this works, but it sorts predictions
    sorted_user_predictions = predictions.iloc[user_row_number].sort_values(ascending=False)
    
    # Get the user's data and merge in the food information.
    user_data = original_ratings[original_ratings.uID == (uID)]
    user_full = (user_data.merge(restaurants, how = 'left', left_on = 'rID', right_on = 'rID').
                     sort_values(['rating'], ascending=False)
                 )

    print ('User {0} has already rated {1} food places.'.format(uID, user_full.shape[0]))
    print ('Recommending the highest {0} predicted food places not already rated.'.format(num_recommendations))
    
    # Recommend the highest predicted food places that the user hasn't seen yet.
    recommendations = (restaurants[~restaurants['rID'].isin(user_full['rID'])].
         merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left',
               left_on = 'rID',
               right_on = 'rID').
         rename(columns = {user_row_number: 'Predictions'}).
         sort_values('Predictions', ascending = False).
                       iloc[:num_recommendations, :-1]
                      )

    return user_full, recommendations

def predict_ratings(R_demeaned, user_ratings_mean, R_df):
    # this does singular value decomposition.. not to sure what that means.. but it works.. 
    # k is the amount of latent factors to approximate original matrix
    print(min(R_demeaned.shape))
    U, sigma, Vt = svds(R_demeaned, k = max(0,min(R_demeaned.shape) - 1))

    # convert to diagonal matrix form, easire for matrix multiplication
    sigma = np.diag(sigma)

    # not quite sure how this fully works either, it does magic to predict what the user would rate the restaurant
    # .. adds users means back to get the predicted rating?
    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    # turn predicted ratings into dataframe
    preds_df = pd.DataFrame(all_user_predicted_ratings, columns = R_df.columns)
    preds_df = pd.DataFrame(all_user_predicted_ratings, columns = R_df.columns)

    return preds_df

# predicts what the user would rate each unrated restaurant
def get_recommendations(userID, num_of_recommendations):
    # parse ratings info and restaurant info
    ratings_list = pd.read_csv('rating_sample.csv', sep=',', names=['uID', 'rID', 'rating'])
    restaurants_list = pd.read_csv('restaurant_sample.csv', sep=',', names=['restaurant','rID', 'sushi','asian','thai','noodles','burgers','western','brazillia','new','ramen','japanese'],  encoding='latin1')

    # cast the appropriate values to be numbers, need to do this or you get int errors
    ratings_list['uID'] = pd.to_numeric(ratings_list['uID'], errors='coerce')
    ratings_list['rID'] = pd.to_numeric(ratings_list['rID'], errors='coerce')

    # make into dataFrame which is a tabular structure
    ratings = pd.DataFrame(ratings_list, columns = ['uID', 'rID', 'rating'], dtype = int)
    restaurants = pd.DataFrame(restaurants_list, columns = ['restaurant','rID', 'sushi','asian','thai','noodles','burgers','western','brazillia','new','ramen','japanese'])

    # cast rID to be int 
    restaurants['rID'] = restaurants['rID'].apply(pd.to_numeric)

    # reformat matrix for 1 col per restaurant and 1 row per user - apparently easire to work with this way
    R_df = ratings.pivot(index = 'uID', columns ='rID', values = 'rating').fillna(0)

    # this normalizes each users mean (de-means the data) and convert from datafram to numpy matrix
    # normalize data for accuracy
    R = R_df.as_matrix()
    user_ratings_mean = np.mean(R, axis = 1)
    R_demeaned = R - user_ratings_mean.reshape(-1, 1)

    preds_df = predict_ratings(R_demeaned, user_ratings_mean, R_df)

    already_rated, predictions = recommend_food(preds_df, userID, restaurants, ratings, num_of_recommendations, restaurants)

    return [already_rated, predictions]

# gonna query the recommender like [{"id": 2, "recommendations": 2}]
# need more than just the users ratings. could return the whole ratings table or a random number of ratings

if __name__ == "__main__":
    # args = parse_args()

    print("starting tailorfood reccomender engine...\n")
    # for x in recommend(args): print(x)

    res = get_recommendations(1, 3)
    # will print the names of the restaurants as well as tne cuisines it fits under
    print(res[1])

    print("\nclosing.")


