#!/bin/bash
msubmenud::opt6() {
  cat <<EOF
This module is used to calculate elastic quantum transport using PWmat and pwmat_transport program, which is based on a unique quantum scattering calculation method. Unlike the NEGF (Non-equilibrium Green's function) method, which scales as O(N3), this scattering state method directly calculates the scattering states at given energy. This method scales linearly to the system size, thus is suitable for large system simulations. It can be used for large device simulation to replace continue mediate approaches like TCAD. This method has been used to study quantum tunneling transistor, and has also been used to calculate interconnect nanojunction with thousands of Cu atoms.（使用散射态方法计算量子输运）
EOF

exit 0
}
