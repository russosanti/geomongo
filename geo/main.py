from geo.utils.PoolManager import PoolManager
from geo.utils.parser import parse_files
from utils.mongodb import init, save

def main():
    init()
    PoolManager()

    countries, states, cities = parse_files()

    save(countries, states, cities)

# Ensure this block is at the end of your script
if __name__ == '__main__':
    main()