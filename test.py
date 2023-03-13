import pandas as pd
import csv
import itertools
import sys
import json

# f = json.loads(str(open("SEA-AD_rui_locations.jsonld", "r")))
# # f = print(type(f))
# print(f)

jsonlds = ['SEA-AD_rui_locations.jsonld','AllenWangLungMap_rui_locations.jsonld','Azimuth-NHLBI-Hourigan-BoneMarrow-rui_locations.jsonld','Azimuth-AllenInstitute-Brain_rui_location.jsonld']

# Opening JSON file
for ruifile in jsonlds:
    f = open(ruifile)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    rui = []
    list = []

    for dict in data:
        

        keys = dict.keys()

        samplelist = dict['samples']
        for sample in samplelist:
            sampleid = sample['@id']
            sample_rui_location= sample['rui_location']
            rui += (sampleid,sample_rui_location)
            print(rui)


# open the file in read mode
filename = open('Untitled spreadsheet - Sheet3.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
csvdatasetid = []
csvsampleid = []
 
# iterating over each row and append
# values to empty list
for col in file:
    csvdatasetid.append(col['dataset_id'])
    csvsampleid.append(col['sample_id'])
 
# printing lists
# print('Month:', csvdatasetid)
# print('Moisturizer:', csvsampleid)

# Closing file
f.close()

print()