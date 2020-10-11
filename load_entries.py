from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
import os
import glob
from os import path
import copy
#load structure enetries as json
import json
with open('save.json', 'r') as f:
    data = json.load(f)

from pymatgen.entries.computed_entries import ComputedEntry,ComputedStructureEntry
entries = [ComputedStructureEntry.from_dict(d) for d in data]
