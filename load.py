import pandas as pd
import geopandas as gpd

class OpenBuildings:
    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file
        self.data = None

    def load_raw(self):
        self.data = pd.read_csv(self.path_to_file)
        self.data['geometry'] = 
        self.data = gpd.GeoDa

