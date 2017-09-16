# tailor-recommender
This is the repo for the python reccomendation engine the app uses heavily.

The engine takes a dataset containing a user's current location, with their favourite restaurants and cuisines, and recommends a restaurant (or cuisine to try, perhaps) to them within their specified radius.

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

bash
```
    $ python3 recommend.py -f restaurants.txt cuisines.txt -num 3
        KATANA, Sushi
        Salad King, Thai
        Five Guys, Burgers
```
