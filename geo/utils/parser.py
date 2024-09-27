import logging
import pandas as pd

from geo import settings
from geo.models.City import City
from geo.models.Country import Country
from geo.models.State import State
from geo.utils.PoolManager import PoolManager
from geo.utils.paths import get_city_data_path, get_country_data_path, get_states_data_path

logging.getLogger().setLevel(logging.INFO)

#########################
#   Parse the cities    #
#########################

def parse_city():
    logging.info("Starting City Parsing")
    df = pd.read_csv(get_city_data_path(), sep='\t', names=City.CITY_FIELDS, header=None, na_values=[], keep_default_na=False)
    df = df[~df.iloc[:, 0].astype(str).str.startswith('#')]
    df[City.ADMIN1] = df[City.COUNTRY_CODE] + '.' + df[City.ADMIN1]
    logging.info("State Parsing finished")
    return df

#########################
#   Parse the states    #
#########################

def parse_state():
    logging.info("Starting State Parsing")
    df = pd.read_csv(get_states_data_path(), sep='\t', names=State.STATE_FIELDS, header=None, usecols=[0, 1, 2], na_values=[], keep_default_na=False)
    df = df[~df.iloc[:, 0].astype(str).str.startswith('#')]
    df[State.COUNTRY] = df['ISO'].str.split('.', expand=True)[0]
    logging.info("State Parsing finished")
    return df

#########################
#  Parse the countries  #
#########################

def parse_country():
    logging.info("Starting Country Parsing")
    df = pd.read_csv(get_country_data_path(), sep='\t', names=Country.COUNTRY_FIELDS, header=None, na_values=[], keep_default_na=False)
    df = df[~df.iloc[:, 0].astype(str).str.startswith('#')]

    if len(settings.ONLY_LANGUAGE) > 0:
        pattern = '|'.join(settings.ONLY_LANGUAGE)
        df = df[df['Languages'].str.contains(pattern, case=False)]

    logging.info("Country Parsing finished")
    return df


def parse_files():
    pool = PoolManager.get_instance().pool
    result_c = pool.apply_async(parse_country)
    result_s = pool.apply_async(parse_state)
    result_ci = pool.apply_async(parse_city)

    countries = result_c.get()
    states = result_s.get()
    cities = result_ci.get()

    return countries, states, cities
