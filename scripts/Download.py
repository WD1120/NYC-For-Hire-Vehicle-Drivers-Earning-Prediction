"""
This script is used to retrieve datasets from the internet
"""

from urllib.request import urlretrieve
import os
from sodapy import Socrata
import pandas as pd
from pyspark.sql import SparkSession, functions as F
import requests, zipfile, io


# Download TLC trip data 
tlc_op = "../data/landing"
if not os.path.exists(tlc_op):
    os.makedirs(tlc_op)

YEARS = ['2022', '2023']
MONTHS = range(1, 13)
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_"#year-month.parquet

for year in YEARS:
    if year == '2023':
        MONTHS = range(1, 4)
    for month in MONTHS:
        month = str(month).zfill(2) 
        url = f'{URL_TEMPLATE}{year}-{month}.parquet'
        output_dir = f"{tlc_op}/{year}-{month}.parquet"
        urlretrieve(url, output_dir)
        print("Downloading", year, month)


# Download timezone
taxi_zone_op = "../data/taxi_zones"
if not os.path.exists(taxi_zone_op):
    os.makedirs(taxi_zone_op)

shp_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip"
req = requests.get(shp_url)
zf = zipfile.ZipFile(io.BytesIO(req.content))
zf.extractall(path=f"{taxi_zone_op}/taxi_zones.shp")
urlretrieve("https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv", taxi_zone_op + "/taxi+_zone_lookup.csv")


# Download external dataset PLUTO
ext_op = "../data/external"
if not os.path.exists(ext_op):
    os.makedirs(ext_op)
client = Socrata("data.cityofnewyork.us", 
                 "BImlKEnhMmlJEIdDC5z4JQzoK",
                 username="diiiiiwu@gmail.com",
                 password="Didiwuhong8416")
    
landuse = client.get("64uk-42ks", limit=860000)
landuse_df = pd.DataFrame.from_records(landuse)
landuse_df.to_parquet(ext_op + '/landuse.parquet')