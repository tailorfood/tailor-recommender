# tailor-recommender
This is the repo for the python reccomendation engine the app uses heavily.

Note: Should probably be weighted

The engine takes a dataset containing a user's current location, with their favourite restaurants and cuisines, and recommends a restaurant (or cuisine to try, perhaps) to them within their specified radius.

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
                    "cuisine": "Thai"
                },
                {
                    "name": "Momofuku Noodle Bar",
                    "cuisine": "Ramen"
                },
                {
                    "name": "McDonald's",
                    "cuisine": "Burgers"
                },
                {
                    "name": "Coco Rice Thai",
                    "cuisine": "Thai"
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
                    "cuisine": "Sushi"
                },
                {
                    "name": "Copacabana Brazilian Steakhouse",
                    "cuisine": "Brazililian"
                },
                {
                    "name": "Five Guys",
                    "cuisine": "Burgers"
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
$ python3 recommend.py -f data.json -u jake -n 3
    KATANA, Sushi
    Salad King, Thai
    Five Guys, Burgers
```

- `-f` is for file that holds all our data
- `-u` is for username
- `-n` is for for the number of return values [(down here in the deep blue sea)](https://www.youtube.com/watch?v=og8NywgVebU)

