from geo.data.CurrencySymbols import CURRENCY_SYMBOLS

 # EquivalentFipsCode

class Country(object):
    ISO = 'ISO'  # ISO
    ISO3 = 'ISO3'  # ISO3
    NUM = 'ISO_Numeric'  # ISO-Numeric
    FIPS = 'fips'  # fips
    COUNTRY = 'Country'  # Country
    CAPITAL = 'Capital'  # Capital
    AREA = 'Area'  # Area(in sq km)
    POPULATOION = 'Population'  # Population
    CONTINENT = 'Continent'  # Continent
    TLD = 'tld'  # tld
    CURRENCRY_CODE = 'Currency_Code'  # CurrencyCode
    CURRENCY_NAME = 'Currency_Name'  # CurrencyName
    PHONE = 'Phone'  # Phone
    ZIP_FORMAT = 'Postal_Code_Format'  # Postal Code Format
    ZIP_REGEX = 'Postal_Code_Regex'  # Postal Code Regex
    LANG = 'Languages'  # Languages
    COUNTRY_ID = 'country_id'  # geonameid
    NEIGHBOURS = 'neighbours'  # neighbours
    EQ_FIPS = 'Equivalent_Fips_Code'
    ID = 'id'

    COUNTRY_FIELDS = [
        ISO,
        ISO3,
        NUM,
        FIPS,
        COUNTRY,
        CAPITAL,
        AREA,
        POPULATOION,
        CONTINENT,
        TLD,
        CURRENCRY_CODE,
        CURRENCY_NAME,
        PHONE,
        ZIP_FORMAT,
        ZIP_REGEX,
        LANG,
        COUNTRY_ID,
        NEIGHBOURS,
        EQ_FIPS
    ]
