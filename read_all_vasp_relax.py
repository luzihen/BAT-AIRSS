from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
import os
import glob
from os import path

entries=[]
uncalculated=[]
dirlist = glob.glob("*/")
for subdir in dirlist:
    os.chdir(subdir)
    print(os.getcwd())
    if path.exists('log'):
        with open('log') as myfile:
            if 'reached' in myfile.read():
                compatibility = MaterialsProjectCompatibility()
                entry_temp=Vasprun('vasprun.xml').get_computed_entry()
                entry_temp = compatibility.process_entry(entry_temp)
                entries.append(entry_temp)
            else:
                uncalculated.append(os.getcwd())
            
        
    else:
        uncalculated.append(os.getcwd())
     
    os.chdir("../")


