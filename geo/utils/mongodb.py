import logging

from pymongo import MongoClient
from urllib.parse import quote_plus

from geo import settings
from geo.models.City import City, city_from_state
from geo.models.Country import Country
from geo.models.State import state_from_country, State
from geo.utils.PoolManager import PoolManager

logging.getLogger().setLevel(logging.INFO)

if settings.MONGO_USER and settings.MONGO_PASSWORD:
    URI = "mongodb://%s:%s@%s:%s/%s" % (quote_plus(settings.MONGO_USER), quote_plus(settings.MONGO_PASSWORD), settings.MONGO_HOST, settings.MONGO_PORT, settings.DB_NAME)
else:
    URI = "mongodb://%s:%s/%s" % (settings.MONGO_HOST, settings.MONGO_PORT, settings.DB_NAME)

MONGO_CLIENT = MongoClient(URI)
DB = MONGO_CLIENT[settings.DB_NAME]
CITY_COLLECTION = DB[settings.CITY_COLLECTION_NAME]
STATE_COLLECTION = DB[settings.STATE_COLLECTION_NAME]
COUNTRY_COLLECTION = DB[settings.COUNTRY_COLLECTION_NAME]

def init():
    CITY_COLLECTION.drop()
    STATE_COLLECTION.drop()
    COUNTRY_COLLECTION.drop()

def save_to_db(mongo_collection, data):
    if not isinstance(data, list):
        raise ValueError('Except data to be a list')

    if not isinstance(data[0], dict):
        raise ValueError('Except item of data to be a dict')

    result = mongo_collection.insert_many(data)

    return result.inserted_ids

def save_cities(country, states, cities):
    logging.info(f"Saving Cities for: {country[Country.COUNTRY]}")
    for _, row in states.iterrows():
        if row['ISO'] == 'AG.09':
            print('Hola')
        c = cities.loc[cities[City.ADMIN1] == row[State.ISO]].copy()

        if c.empty:
            c = city_from_state(country, row)

        c['country'] = country['id']
        c['state'] = row['id']
        save_to_db(CITY_COLLECTION, c[settings.CITY_FIELDS_TO_SAVE].to_dict(orient='records'))

    logging.info(f"Finished saving States for: {country[Country.COUNTRY]}")

def save_states(countries, states, cities):
    pool = PoolManager.get_instance().pool
    for _, row in countries.iterrows():
        logging.info(f"Saving States for: {row[State.ISO]}")
        s = states.loc[states[State.COUNTRY] == row[Country.ISO]].copy()

        if s.empty:
            s = state_from_country(row)

        s['country'] = row['id']
        sids = save_to_db(STATE_COLLECTION, s[settings.STATE_FIELDS_TO_SAVE].to_dict(orient='records'))
        s['id'] = sids
        pool.apply_async(save_cities, args=(row, s, cities))
        logging.info(f"Finished saving States for: {row[State.ISO]}")

def save(countries, states, cities):
    logging.info("Saving Countries")
    s = countries[settings.COUNTRY_FIELDS_TO_SAVE]
    ids = save_to_db(COUNTRY_COLLECTION, s.to_dict(orient='records'))
    countries.loc[:, Country.ID] = ids
    logging.info("Finished Saving Countries")
    save_states(countries, states, cities)