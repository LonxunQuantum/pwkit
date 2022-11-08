#!/bin/bash
msubmenud::opt3() {
  cat <<EOF
This module is the interface between PWmat and Boltzwann, which can be used to calculate the transport properties, including electrical and thermal conductivities, Seebeck coefficient. It should be noted that BolztWann code has tightly integrated with the Wannier90 code（与Boltzwann的接口，可以计算热输运性质，比如热导，电导，塞贝克系数等）
EOF

exit 0
}
