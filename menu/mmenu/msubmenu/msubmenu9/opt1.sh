#!/bin/bash
msubmenu9::opt1() {
  cat <<EOF
This module is used to calculate elastic constants by high-throughout method. ELPWmat is an efficient open source python program using PWmat to calculate elastic constants, compliance constants, Young's, shear and bulk moduli and Poisson's ratio for 3D materials and 2D materials via high-throughput first-principles computation. For 3D materials, ELPWmat can calculate elastic constants, compliance constants, the polycrystalline Young's, shear and bulk moduli and Poisson's ratio, according to Voigt-Reuss-Hill's approximations. For 2D materials, ELPWmat can calculate elastic constants, compliance constants, in-plane Young's, shear moduli and in-plane Poisson's ratio.（计算3D材料和2D材料的弹性常数，顺应常数，杨氏，剪切模量和体积模量以及泊松比））
EOF

exit 0
}
