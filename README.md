# tailor-recommender
This is the repo for the python reccomendation engine the app uses heavily.

Note: Should probably be weighted

The engine takes a dataset containing a user's current location, with their favourite restaurants and cuisines, and recommends a restaurant (or cuisine to try, perhaps) to them within their specified radius.

# Current Working State

Using the sample data, can quiry on a userID and ask for `n` recommendations.

### Potential goodies

- http://surpriselib.com/
- http://pandas.pydata.org/
- https://turi.com/

### Example

data.json
```
{
    "users": [
        {
            "username": "jake",
            "location": {
                "lat": 42.123123,
                "lon": 45.131555
            },
            "radius": 10,
            "restaurants": [
                {
                    "name": "Pai Northern Kitchen",
                    "cuisine": "Thai",
                    "like": true
                },
                {
                    "name": "Momofuku Noodle Bar",
                    "cuisine": "Ramen",
                    "like": false
                },
                {
                    "name": "McDonald's",
                    "cuisine": "Burgers",
                    "like": true
                },
                {
                    "name": "Coco Rice Thai",
                    "cuisine": "Thai",
                    "like": true
                }
            ],
            "cuisines": [ "Thai", "Ramen", "Burgers" ]
        },
        {
            "username": "jason",
            "location": {
                "lat": 42.123123,
                "lon": 45.131555
            },
            "radius": 12,
            "restaurants": [
                {
                    "name": "Fushimi",
                    "cuisine": "Sushi",
                    "like": true
                },
                {
                    "name": "Copacabana Brazilian Steakhouse",
                    "cuisine": "Brazililian",
                    "like": true
                },
                {
                    "name": "Five Guys",
                    "cuisine": "Burgers",
                    "like": false
                }
            ],
            "cuisines": [ "Sushi", "Brazililian", "Burgers" ]
        }
    ],
    "keys": {
        "GOOGLE_KEY": <key>,
        "YELP_ID": <key>,
        "YELP_SECRET": <key>
    }
}
```

bash

```
$ ./recommend.py -n 3 -u jake -f data.json
starting tailorfood reccomender engine...

{'name': 'KATANA', 'cuisine': 'Sushi'} (cuisine like Ramen)
{'name': 'Salad King', 'cuisine': 'Ramen'} (restaurant like Pai Northern Kitchen)
{'name': 'Five Guys', 'cuisine': 'Burgers'} (restaurant and cuisine like McDonald's)

closing.
```

- `-f` is for file that holds all our data  - "I'm not sure if `-f` is a good cmd-line flag to use, it's often a keyword used in
                                              UNIX command lines and Git
- `-u` is for username
- `-n` is for for the number of return values [(down here in the deep blue sea)](https://www.youtube.com/watch?v=og8NywgVebU)

