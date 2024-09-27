import urllib.request
import zipfile
import shutil
import os
import logging

from utils.paths import get_country_data_path, get_city_data_path, get_states_data_path


def download_file(url, file_name):
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

def unzip_file(path_to_zip_file, directory_to_extract_to):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()

def save_file():
    logging.info("Starting Country download")
    country_file_name = 'countryInfo.txt'
    download_file('http://download.geonames.org/export/dump/countryInfo.txt', country_file_name)
    shutil.copy(country_file_name, get_country_data_path())
    os.remove(os.path.join(os.getcwd(), country_file_name))
    logging.info("Country download finished")

def save_zip():
    logging.info("Starting City download")
    cities_zip_file_name = 'cities500.zip'
    cities_file_name = 'cities500.txt'
    download_file('http://download.geonames.org/export/dump/cities500.zip', cities_zip_file_name)
    logging.info("City download finished")
    logging.info("Unziping and copying")
    unzip_file(cities_zip_file_name, os.getcwd())
    shutil.copy(cities_file_name, get_city_data_path())
    os.remove(cities_zip_file_name)
    os.remove(cities_file_name)
    logging.info("Done")


def save_states():
    logging.info("Starting States download")
    cities_file_name = 'admin1CodesASCII.txt'
    download_file('http://download.geonames.org/export/dump/admin1CodesASCII.txt', cities_file_name)
    shutil.copy(cities_file_name, get_states_data_path())
    os.remove(os.path.join(os.getcwd(), cities_file_name))
    logging.info("Country download finished")
    logging.info("Unziping and copying")

logging.getLogger().setLevel(logging.INFO)
save_file()
save_states()
save_zip()