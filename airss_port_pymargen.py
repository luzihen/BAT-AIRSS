from pymatgen import MPRester, Composition, Element
#from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import PhaseDiagram, CompoundPhaseDiagram, PDPlotter
from pymatgen.entries.computed_entries import ComputedEntry, ComputedStructureEntry
import json
import re
import palettable
import matplotlib as mpl1
from pymatgen.io.cif import CifParser
from pymatgen.core.structure import IStructure

#ComputedEntry(composition: pymatgen.core.composition.Composition, energy: float, correction: float = 0.0, energy_adjustments: list = None, parameters: dict = None, data: dict = None, entry_id: object = None)
#IStructure.from_file('LiB-42129-4374-9-out.cif')
#ComputedStructureEntry(structure=IStructure.from_file('LiB-42129-4374-9-out.cif'),energy=1,entry_id='from castep for airss')


import os
current_dir = os.getcwd()

entries=[]
for filename in os.listdir(current_dir):
    if filename.endswith(".res"):
        print('loading ', filename)
        #read enthalpy, did not correct enthalpy for pressure
        f = open(filename, "r")
        enthalpy=f.readline().split()[4]
        f.close()
        #load structure and composition, cabal in airss is needed
        os.system("cabal res poscar < "+filename+" > POSCAR")
        entries.append(ComputedStructureEntry(structure=IStructure.from_file('POSCAR'), energy=float(enthalpy)))
        os.system("rm POSCAR")


#pd=PhaseDiagram(entries)
#pd.show()


#li_entries = [e for e in entries if e.composition.reduced_formula == "Li"]
#uli0 = min(li_entries, key=lambda e: e.energy_per_atom).energy_per_atom
#gpd=GrandPotentialPhaseDiagram(entries,chempots=)
