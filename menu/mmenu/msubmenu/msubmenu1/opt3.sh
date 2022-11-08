#!/bin/bash
msubmenu1::opt3() {
  cat <<EOF
This module is used to introduce how to use Genetic Algorithm to search generate
new structures of the absorbed molecule/cluster,
while keeping the structure of the substrate unchanged (although it will be moved during relaxation).
For example, it can be used to search: water molecules around –CO adsorbed on Cu(111) surface;
metal cluster with given number of atoms; atomic structure of interfacial region between two materials;
water pattern on a flat metal surface;
water pattern on a spherical metal nano-cluster; ...（用基因遗传算法搜索表面结构，例如用于表面催化）
EOF

exit 0
}
