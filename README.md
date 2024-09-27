# world-cities-mongodb

Do you want a database which contains most of cities in the world as well as the countries? This app will save 3 collections to your mongodb:

 1. `cities`
 1. `states`
 1. `countries`

## Why use it

 - Language agnostic because it's not a lib. Consume the result database using any language you like.
 - Source data from [GeoNames.org](http://www.geonames.org/) is under active updates. And this app will let you update in few seconds.
 - `python main.py` to generate the database from source data
 - `python update.py` to update the source data from GeoNames
 - Remove any fields you don't need in `settings.py`
 - Could filter countries which only speak certain languages. (see `setting.py`)

## Python version

- Python 3
- Python 2 should be fine, but haven't tried.

## How to use

1. `git clone`

1. `pip install` uses requirements.txt

1. Open `settings.py`, set up your database settings.

1. `python main.py`

1. Enjoy :)

- To update the source data in `data` folder: **`python update.py`**

## Folder Structure

- `[data]`: [Folder] Raw data from GeoNames
- `[models]`: [Folder] database fields for city and country
- `[utils]`: [Folder] Helper function
- `settings.py`: Settings
- `main.py`: Main file to generate the database
- `update.py`: Update the source `data` from GeoNames

## About the data

- The data is from [GeoNames](http://www.geonames.org/).

- The `cities` contains cities which population greater than 500.

- How to update the data
  - **`python update.py`**
