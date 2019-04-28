import pymatgen as mg
import json
import numpy as np
from pymatgen.electronic_structure.bandstructure import *
from pymatgen.ext.matproj import MPRester
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSPlotter

with open('b.json', 'r') as f:
    d = json.load(f)
    bs = BandStructureSymmLine.from_dict(d)

print(type(bs))

plotter = BSPlotter(bs)
plotter.get_plot().show()



