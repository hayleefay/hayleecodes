# Creating a script that inputs the bilateral csv into my django psqldb

import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hayleecodes.settings')
django.setup()

from mysite.models import Bilateral

bilateral_data = pd.read_csv('django_app/bilateral_flow.csv', low_memory=False)

for index, row in bilateral_data.iterrows():
    region_orig = row[0]
    region_orig_id = row[1]
    region_dest = row[2]
    region_dest_id = row[3]
    country_orig = row[4]
    country_orig_id = row[5]
    country_dest = row[6]
    country_dest_id = row[7]
    regionflow_1990 = row[8]
    regionflow_1995 = row[9]
    regionflow_2000 = row[10]
    regionflow_2005 = row[11]
    countryflow_1990 = row[12]
    countryflow_1995 = row[13]
    countryflow_2000 = row[14]
    countryflow_2005 = row[15]
    metadata = row[16]

    q = Bilateral(region_orig = region_orig, region_orig_id = region_orig_id, region_dest = region_dest, \
    region_dest_id = region_orig_id, country_orig = country_orig, country_orig_id = country_orig_id, \
    country_dest = country_dest, country_dest_id = country_dest_id, regionflow_1990 = regionflow_1990, \
    regionflow_1995 = regionflow_1995, regionflow_2000 = regionflow_2000, regionflow_2005 = regionflow_2005, \
    countryflow_1990 = countryflow_1990, countryflow_1995 = countryflow_1995, countryflow_2000 = countryflow_2000, \
    countryflow_2005 = countryflow_2005, metadata = metadata)

    q.save()
