from pflow.io.publicLayer.structure import DStructure
import numpy as np


### Part I.
structure = DStructure.from_file(
    file_format="pwmat", 
    file_path="/data/home/liuhanyu/hyliu/pwmat_demo/band/atom.config",
)
basis = np.array(structure.lattice.reciprocal_lattice.matrix)
print("\n倒格矢 (unit: 1/(2*pi)) : ")
print(basis)

print("\n倒格矢 : ")
print(np.array(structure.lattice.reciprocal_lattice_crystallographic.matrix))


### Part II.
a1 = np.array([
      [0.000000,      0.000000,      0.000000],
      [0.055556,      0.000000,      0.000000],           
      [0.111111,      0.000000,      0.000000],         
      [0.166667,      0.000000,      0.000000],        
      [0.222222,      0.000000,      0.000000],
            ])
print("\n计算结果 : ")
print( np.dot(a1, basis) * 0.529177249 )