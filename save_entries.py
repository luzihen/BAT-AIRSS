from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
import os
import glob
from os import path
import copy
import json
all=[]
for entry in entries:
    all.append(entry.as_dict())

with open('save.json','w') as f:
    json.dump(all, f)       
