import pandas as pd
import csv
import itertools
import sys
import json
import pprint

# f = json.loads(str(open("SEA-AD_rui_locations.jsonld", "r")))
# # f = print(type(f))
# print(f)

jsonlds = ['SEA-AD_rui_locations.jsonld','AllenWangLungMap_rui_locations.jsonld','Azimuth-NHLBI-Hourigan-BoneMarrow-rui_locations.jsonld','Azimuth-AllenInstitute-Brain_rui_location.jsonld','ccf-hca-rui-locations.jsonld']

rui = []
# Opening JSON file
for ruifile in jsonlds:
    f = open(ruifile)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    
    list = []

    for dict in data:
        

        keys = dict.keys()

        samplelist = dict['samples']
        for sample in samplelist:
            sampleid = sample['@id']
            sample_rui_location= sample['rui_location']
            rui += [[sampleid,sample_rui_location]]
            # print(rui)

print(rui)
# open the file in read mode
filename = open('CTPop datasets - ccf_sample_id.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
csvrows = []
 
# iterating over each row and append
# values to empty list
for col in file:
    csvrows.append([col['dataset_id'],col['sample_id']])

outputJSON = {}

for row in csvrows:
    # print(row[0])
    csv_sample_id = row[1]
    for pair in rui:
        if csv_sample_id == pair[0]:
            row_dict = {}
            row_dict['sample_id'] = pair[0]
            row_dict['rui_location'] = pair[1]
            print(row_dict)
            outputJSON[row[0]] = row_dict 

pprint.pprint(outputJSON)

with open("CTPop_all_datasets_3-20-2023.json", "w") as outfile:
    json.dump(outputJSON, outfile)

            
    
     
# printing lists
# print('CSV rows:', csvrows)

# Closing file
f.close()
