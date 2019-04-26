import pymatgen as mg
import json

from pymatgen.electronic_structure.bandstructure import BandStructureSymmLine
from pymatgen.ext.matproj import MPRester
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSPlotter

# This initiliazes the Rest connection to the Materials Project db. Put your own API key if needed.
a = MPRester("cpbACRSpLraOORKv8yNQ")
# load the band structure from mp-3748, CuAlO2 from the MP db
bs = a.get_bandstructure_by_material_id("mp-3748")

# is the material a metal (i.e., the fermi level cross a band)
# print(bs.is_metal())
# # print information on the band gap
# print(bs.get_band_gap())
# # print the energy of the 20th band and 10th kpoint
# print(bs.bands[Spin.up][20][10])
# print energy of direct band gap
# print(bs.get_direct_band_gap())
# # print information on the vbm
# print(bs.get_vbm())


# with open('a.json', 'r', encoding='UTF-8') as f:
#     print(type(f.read()))
#     s = f.read()
#     json.dumps(s)
#     d = json.loads(s)
#     bs = BandStructureSymmLine.from_dict(d)
# list1 = BandStructureSymmLine.as_dict(bs)
# print(list1)
print(type(bs))
# print(type(list1))

plotter = BSPlotter(bs)
plotter.get_plot().show()
