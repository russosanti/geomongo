import pandas as pd

from geo.models.Country import Country

def state_from_country(country):
    return pd.DataFrame(
        [[country[Country.ISO] + ".01", country[Country.COUNTRY], country[Country.COUNTRY], country[Country.ISO]]],
        columns=[State.ISO, State.NAME, State.ASCII_NAME, State.COUNTRY])

class State(object):
    ISO = 'ISO'  # ISO
    NAME = 'Name'  # ISO3
    ASCII_NAME = 'ASCII_Name'  # ISO-Numeric
    COUNTRY = 'Country'

    STATE_FIELDS = [
        ISO,  # ISO
        NAME,  # ISO3
        ASCII_NAME  # ISO-Numeric
    ]