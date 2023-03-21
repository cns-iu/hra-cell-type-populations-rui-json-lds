import pandas as pd
import csv
import json
import os
import urllib
from urllib.parse import urlparse
from pathlib import Path
from getgsheet import *

### import JSON.ld files #! Needs to be updated and programmatically pull from ccf-api. Currently pulls from static data in dw-dot GitHub

# url = "https://ccf-api.hubmapconsortium.org/v1/gtex/rui_locations.jsonld"
# u = urlparse(url)
# print(u.path)

###push all jsonld files from current directory to list
jsonlds = []
directory = Path.cwd()
      
for filename in os.listdir(directory):
    if filename.endswith(".jsonld") :
        jsonlds.append(str(filename))

print(jsonlds)

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

### download local copy of csv from Google Sheet

# define google sheet param
doc_id = '1cwxztPg9sLq0ASjJ5bntivUk6dSKHsVyR1bE6bXvMkY'
sheet_id = '1529271254'
google_sheet_title = 'google-sheet.csv'

#build csv and open in read mode
build_local_csv_from_gsheet(doc_id,sheet_id, google_sheet_title)
local_gsheet_as_csv = open(google_sheet_title, 'r')

#filtering columns & creating dictreader object & removing row 1 (all whitespace)
columns = ["dataset_id", "sample_id"]
df = pd.read_csv(local_gsheet_as_csv, skiprows=[0], usecols=columns)
df.to_csv("google-sheet_dataset_id_and_sample_id.csv", index=False)



# iterating over each row and append key-value pairs to empty dict
file = csv.DictReader(open('google-sheet_dataset_id_and_sample_id.csv', 'r'))

csvrows = []
for col in file:
    print(col)
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
            # print(row_dict)
            outputJSON[row[0]] = row_dict 


#print readable JSON
# pprint.pprint(outputJSON)

#Write JSON into current dir
with open("CTPop_all_datasets_3-20-2023.json", "w") as outfile:
    json.dump(outputJSON, outfile)

# Closing file
f.close()
local_gsheet_as_csv.close()
