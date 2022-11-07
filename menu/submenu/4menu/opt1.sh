#!/bin/bash
submenu::4opt1() {
  cat <<EOF
This module is the interface between PWmat and CIF2CELL.
CIF2CELL is a tool to generate the geometrical setup for various electronic structure codes
from a CIF (Crystallographic Information Framework) file.
The program currently supports output for a number of popular electronic structure programs,
including PWmat, ABINIT, ASE, CASTEP, CP2K, CPMD, CRYSTAL09, Elk, EMTO, Exciting, Fleur, FHI-aims,
Hutsepot, MOPAC, Quantum Espresso, RSPt, Siesta, SPR-KKR, VASP. Also exports some related formats
like .coo, .cfg and .xyz-files.（将cif文件转换为atom.config））
EOF

exit 0
}