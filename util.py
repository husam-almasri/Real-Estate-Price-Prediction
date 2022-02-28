import json
import pickle
import numpy as np

__locations = None
__areas = None
__data_columns = None
__model = None


def get_location_names():
    return __locations

def get_area_names():
    return __areas


def get_estimated_price(bedrooms, total_sqft, bath, balcony, area_type, location):
    try:
        area_type_index = __data_columns.index(area_type.lower())
        location_index = __data_columns.index(location.lower())
    except:
        area_type_index = -1
        location_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = total_sqft
    x[2] = bath
    x[3] = balcony
    if area_type_index >= 0:
        x[area_type_index] = 1
    if location_index >= 0:
        x[location_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print('Loading saved artifacts...start')
    global __model
    global __data_columns
    global __locations
    global __areas

    with open('./artifacts/columns.json') as f:
        __data_columns = json.load(f)['data_columns']
        __areas = __data_columns[4:8]
        __locations = __data_columns[8:]
    with open('./artifacts/house_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('Loading saved artifacts...done')


if __name__ == "__main__":
    load_saved_artifacts()

