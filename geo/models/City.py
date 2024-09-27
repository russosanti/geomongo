from datetime import datetime

import pandas as pd

from geo.models.State import State

class City(object):

    CITY_ID = 'city_id' # integer id of record in geonames database
    NAME = 'name' # name of geographical point (utf8) varchar(200)
    ASCII_NAME = 'ascii_name' # name of geographical point in plain ascii characters, varchar(200)
    ALT_NAMES = 'alternate_names' # alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
    LAT = 'latitude' #latitude in decimal degrees (wgs84)
    LON = 'longitude' # longitude in decimal degrees (wgs84)
    CLASS = 'feature_class' # see http://www.geonames.org/export/codes.html, char(1)
    CLASS_CODE = 'feature_code' # see http://www.geonames.org/export/codes.html, varchar(10)
    COUNTRY_CODE = 'country_code' # ISO-3166 2-letter country code, 2 characters
    CC2 = 'cc2' # alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
    ADMIN1 = 'admin1_code' # fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
    ADMIN2 = 'admin2_code' # code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
    ADMIN3 = 'admin3_code' # code for third level administrative division, varchar(20)
    ADMIN4 = 'admin4_code' # code for fourth level administrative division, varchar(20)
    POUPULATION = 'population' # bigint (8 byte int)
    ELEVATION = 'elevation' # in meters, integer
    DEM = 'dem' # digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
    TIMEZONE = 'timezone' # the iana timezone id (see file timeZone.txt) varchar(40)
    MODIFICATION_DATE = 'modification_date' # date of last modification in yyyy-MM-dd format

    CITY_FIELDS = [
        CITY_ID,
        NAME,
        ASCII_NAME,
        ALT_NAMES,
        LAT,
        LON,
        CLASS,
        CLASS_CODE,
        COUNTRY_CODE,
        CC2,
        ADMIN1,
        ADMIN2,
        ADMIN3,
        ADMIN4,
        POUPULATION,
        ELEVATION,
        DEM,
        TIMEZONE,
        MODIFICATION_DATE
    ]


def city_from_state(country, state):
    return pd.DataFrame({
        City.CITY_ID: state[State.ISO],
        City.NAME: state[State.NAME],
        City.ASCII_NAME: state[State.ASCII_NAME],
        City.ALT_NAMES: pd.NA,
        City.LAT: pd.NA,
        City.LON: pd.NA,
        City.CLASS: "P",
        City.CLASS_CODE: "PPL",
        City.COUNTRY_CODE: state[State.COUNTRY],
        City.CC2: pd.NA,
        City.ADMIN1: state[State.ISO],
        City.ADMIN2: pd.NA,
        City.ADMIN3: pd.NA,
        City.ADMIN4: pd.NA,
        City.POUPULATION: pd.NA,
        City.ELEVATION: pd.NA,
        City.DEM: pd.NA,
        City.TIMEZONE: pd.NA,
        City.MODIFICATION_DATE: datetime.now().strftime("%Y-%m-%d")
    }, index=[0])