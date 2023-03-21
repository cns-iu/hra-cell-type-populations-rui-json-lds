from pathlib import Path
import os

directory = Path.cwd()
      
for filename in os.listdir(directory):
    if filename.endswith(".jsonld") :
        print(filename)