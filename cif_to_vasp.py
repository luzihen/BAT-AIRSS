from pymatgen import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.io.vasp.sets import batch_write_input, MPRelaxSet
import os
from pymatgen.io.vasp.inputs import Kpoints

for file in os.listdir():
    if file.endswith(".cif"):
        structure = Structure.from_file(file)
        relax = MPRelaxSet(structure)
        relax.write_input(file.replace('.cif',''))
    
