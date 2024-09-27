from geo.models.City import City
from geo.models.Country import Country
from geo.models.State import State

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USER = ''
MONGO_PASSWORD = ''
DB_NAME = 'test'

CITY_COLLECTION_NAME = 'cities'
STATE_COLLECTION_NAME = 'states'
COUNTRY_COLLECTION_NAME = 'countries'

# Only countries with languages below.
# Find the languages here:
# http://www.lingoes.net/en/translator/langcode.htm
# city.country_code and country.iso MUST be there in order to enable this feature.
# Below is an example for only save all English speaking countries.
ONLY_LANGUAGE = [
    # 'en',
    # 'en-AU', 'en-BZ', 'en-CA', 'en-CB',
    # 'en-GB', 'en-IE', 'en-JM', 'en-NZ',
    # 'en-PH', 'en-TT', 'en-US', 'en-ZA',
    # 'en-ZW'
]

# Add the name of field that you want to save
CITY_FIELDS_TO_SAVE = [
    City.NAME,
    City.ASCII_NAME,
    City.ALT_NAMES,
    City.LAT,
    City.LON,
    City.COUNTRY_CODE,
    City.ADMIN1,
    City.TIMEZONE,
    'country',  # Country ID
    'state'  # State ID
]

# Add the name of field that you want to save
STATE_FIELDS_TO_SAVE = [
    State.ISO,  # ISO
    State.NAME,  # ISO3
    State.ASCII_NAME,  # ISO-Numeric
    State.COUNTRY,
    'country' # Country ID
]

# Add the name of field that you want to save
COUNTRY_FIELDS_TO_SAVE = [
    Country.ISO,
    Country.ISO3,
    Country.COUNTRY,
    Country.CAPITAL,
    Country.CONTINENT,
    Country.CURRENCRY_CODE,
    Country.CURRENCY_NAME,
    Country.PHONE,
    Country.ZIP_REGEX,
    Country.LANG
]