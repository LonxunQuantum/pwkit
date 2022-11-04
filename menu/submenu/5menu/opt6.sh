#!/bin/bash
submenu::5opt6() {
  cat <<EOF
This module introduce a new, second order k-point interpolation scheme.
It can be used to plot the band structure. But it can also be used to do other k-point
integration scheme over the Brillouin Zone. Compared to previous interp_absorption,
and interp_DOS method, this one is more accurate. But it is also more expensive.
Future improvement using GPU might be necessary. It can be used for any Hamiltonian,
e.g., DFT+U, or HSE etc.（一种新的二阶插值方法，与之前的方法相比，这种插值方法更精确，适用范围更广，计算量也更大）
EOF

exit 0
}
