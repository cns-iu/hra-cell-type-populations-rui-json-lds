import pandas as pd
import csv
import itertools
import sys
import json
import pprint

# f = json.loads(str(open("SEA-AD_rui_locations.jsonld", "r")))
# # f = print(type(f))
# print(f)

jsonlds = ['ccf-hca-rui-locations.jsonld']
# jsonlds = ['SEA-AD_rui_locations.jsonld','AllenWangLungMap_rui_locations.jsonld','Azimuth-NHLBI-Hourigan-BoneMarrow-rui_locations.jsonld','Azimuth-AllenInstitute-Brain_rui_location.jsonld','ccf-hca-rui-locations.jsonld']

# Opening JSON file
for ruifile in jsonlds:
    f = open(ruifile)
    
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    
    
list = {}
for row in data:
    samples = row['samples'][0]
    rui = samples['rui_location']
    row_dict = {}
    # print(row)
    
    row_dict['sample_id'] = samples['@id']
    row_dict['x_dimension'] = rui['x_dimension']
    row_dict['y_dimension'] = rui['y_dimension']
    row_dict['z_dimension'] = rui['z_dimension']
    row_dict['block_volume'] = (int(rui['x_dimension'])*int(rui['y_dimension'])*int(rui['z_dimension']))
    print(row_dict)
    list[samples['@id']] = row_dict

pprint.pprint(list)

with open("sample.json", "w") as outfile:
    json.dump(list, outfile)

            
    
     
# printing lists
# print('CSV rows:', csvrows)

# Closing file
f.close()
