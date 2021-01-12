#for same composition
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.entries.computed_entries import ComputedEntry

import os

entries=[]
rootdir = os.getcwd()
directory_contents = os.listdir(rootdir)
for dir in directory_contents:
    if os.path.isdir(dir):
        os.chdir(dir)
        if os.path.isfile("vasprun.xml"):
            print ("File exist")
            vrun=Vasprun("vasprun.xml")
            entry_temp=vrun.get_computed_entry()
            entry_temp.entry_id=dir
            entries.append(entry_temp)
        os.chdir("../")

entries_sorted=sorted(entries, key=lambda entry: entry.energy_per_atom)   # sort by age

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
