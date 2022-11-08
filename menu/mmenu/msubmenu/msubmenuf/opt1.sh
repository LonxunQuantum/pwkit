#!/bin/bash
msubmenuf::opt1() {
  cat <<EOF
This module is used to introduce how to run YAMBO to get GW quasi-particle energy based on PWmat DFT results. YAMBO implements Many-Body Perturbation Theory (MBPT) methods (such as GW and BSE) and Time-Dependent Density Functional Theory (TDDFT), which allows for accurate prediction of fundamental properties as band gaps of semiconductors, band alignments, defect quasi-particle energies, optics and out-of-equilibrium properties of materials.（介绍如何使用pwmat+yambo进行GW计算）
EOF

exit 0
}
