# tailor-recommender
This is the repo for the python reccomendation engine the app uses heavily.

Note: Should probably be weighted

The engine takes a dataset containing a user's current location, with their favourite restaurants and cuisines, and recommends a restaurant (or cuisine to try, perhaps) to them within their specified radius.

### Potential goodies

- http://surpriselib.com/
- http://pandas.pydata.org/
- https://turi.com/

### Example

**Note:** the format of the data is subject to change

restaurants.txt (sorted favourite-first)
```
Pai Northern Kitchen, Thai
JaBistro, Sushi
Momofuku Noodle Bar, Ramen
McDonald's, Burgers
Coco Rice Thai, Thai
```

cuisines.txt (sorted favourite-first)
```
Thai
Ramen
Burgers
Sushi
```

keys.txt (': ' is important for formatting)
```
GOOGLE_KEY: <key>
YELP_KEY: <key>
YELP_SECRET: <key>
YELP_TOKEN: <key>
YELP_TOKEN_SECRET: <key>
```

bash

```
$ python3 recommend.py -r restaurants.txt -c cuisines.txt -k keys.txt -l toronto --radius 10 --num 3
    KATANA, Sushi
    Salad King, Thai
    Five Guys, Burgers
```

- `-r` for restaurants
- `-c` for cuisines
- `-k` for (API) keys
- `-l` for location
- `--radius` for radius, in km
- `--num` for number of result restaurants requested 